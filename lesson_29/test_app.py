import pytest
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

def test_insert_and_select():
    row_id = insert_row('test', 123)
    rows = select_rows()
    assert len(rows) == 1
    assert rows[0][0] == row_id
    assert rows[0][1] == 'test'
    assert rows[0][2] == 123

def test_update():
    row_id = insert_row('test', 123)
    update_row(row_id, 456)
    rows = select_rows()
    assert rows[0][2] == 456

def test_delete():
    row_id = insert_row('test', 123)
    delete_row(row_id)
    rows = select_rows()
    assert len(rows) == 0

def test_connection():
    try:
        with get_connection() as conn:
            assert conn is not None
    except Exception as e:
        pytest.fail(f"Connection failed: {e}")
