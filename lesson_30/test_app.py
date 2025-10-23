
import pytest
import allure
from app import create_table, insert_row, update_row, delete_row, select_rows, get_connection

@pytest.fixture(scope="module", autouse=True)
def setup_db():
    create_table()
    yield

@pytest.fixture(autouse=True)
def clean_table():
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute('DELETE FROM test_table')
            conn.commit()

@allure.feature("Insert and Select")
def test_insert_and_select():
    with allure.step("Insert row into table"):
        row_id = insert_row('test', 123)
    with allure.step("Select rows from table"):
        rows = select_rows()
    with allure.step("Check inserted row"):
        assert len(rows) == 1
        assert rows[0][0] == row_id
        assert rows[0][1] == 'test'
        assert rows[0][2] == 123

@allure.feature("Update row")
def test_update():
    with allure.step("Insert row for update"):
        row_id = insert_row('test', 123)
    with allure.step("Update row value"):
        update_row(row_id, 456)
    with allure.step("Check updated value"):
        rows = select_rows()
        assert rows[0][2] == 456

@allure.feature("Delete row")
def test_delete():
    with allure.step("Insert row for delete"):
        row_id = insert_row('test', 123)
    with allure.step("Delete row"):
        delete_row(row_id)
    with allure.step("Check table is empty"):
        rows = select_rows()
        assert len(rows) == 0

@allure.feature("DB Connection")
def test_connection():
    with allure.step("Try to connect to DB"):
        try:
            with get_connection() as conn:
                assert conn is not None
        except Exception as e:
            pytest.fail(f"Connection failed: {e}")
