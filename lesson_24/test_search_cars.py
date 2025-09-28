import pytest
import requests
import logging
from requests.auth import HTTPBasicAuth

BASE_URL = "http://127.0.0.1:8080"

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("test_search.log")
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)


@pytest.fixture(scope="class")
def auth_session():
    session = requests.Session()
    url = f"{BASE_URL}/auth"
    auth = HTTPBasicAuth("test_user", "test_pass")

    response = session.post(url, auth=auth)

    assert response.status_code == 200, f"Auth failed: {response.text}"

    access_token = response.json().get("access_token")
    session.headers.update({"Authorization": f"Bearer {access_token}"})
    return session


@pytest.mark.usefixtures("auth_session")
class TestCarSearch:

    @pytest.mark.parametrize("sort_by,limit", [
        ("price", 5),
        ("year", 3),
        ("engine_volume", 10),
        ("engine_volume", 1),
        ("brand", 7),
        ("price", 0),
        ("year", 25),
        ("brand", 26),
        ("nonexistent_field", 5)
    ])
    def test_search_cars(self, auth_session, sort_by, limit):
        print()
        log_message = f"TEST: GET /cars?sort_by={sort_by}&limit={limit}"
        logger.info(log_message)

        url = f"{BASE_URL}/cars"
        params = {"sort_by": sort_by, "limit": limit}

        response = auth_session.get(url, params=params)
        data = response.json()

        sorting_passed = None

        def log_result(level="info", status=None, reason=None):

            if status == "pass":
                logger.info("Sorting check: pass")
            elif status == "fail":
                logger.error("Sorting check: fail")
            else:
                logger.warning("Sorting check: skipped")

            logger.info(f"Returned: {len(data)}")

            logger.info(f"Response code: {response.status_code}")

            if reason:
                logger.error(f"Reason: {reason}")

        try:
            assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
            assert isinstance(data, list), "Response should be a list"
            assert len(data) <= limit, f"Limit exceeded: expected ≤{limit}, got {len(data)}"

            if data and sort_by in data[0]:
                values = [item[sort_by] for item in data]
                logger.info(f"Values for sorting': {values}")
                assert values == sorted(values), f"Data not sorted by {sort_by}: {values}"
                sorting_passed = True
            else:
                logger.warning(f"Field '{sort_by}' not found in response")

            log_result(status="pass" if sorting_passed else None)
            logger.info("TEST PASSED")

        except AssertionError as e:
            status = "fail" if sorting_passed is False else None
            log_result(status=status, reason=f"{type(e).__name__}: {e}")
            logger.error("TEST FAILED")
            raise
        finally:
            logger.info("-" * 50)