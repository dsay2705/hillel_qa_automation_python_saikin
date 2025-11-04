from ..pages.tracking_page import TrackingPage
from ..settings import settings

def test_tracking_status_charged(browser):
    tracking_number = settings.get("TRACKING_NUMBER")
    expected_status = "Отримана"

    page = TrackingPage(browser)
    page.open()
    page.enter_tracking_number(tracking_number)
    page.click_search_button()

    actual_status = page.get_status()

    assert actual_status == expected_status, f"Expected: {expected_status}, got: {actual_status}"