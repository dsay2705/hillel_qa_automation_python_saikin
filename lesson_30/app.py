import os
import psycopg2

DB_HOST = os.environ.get('DB_HOST', 'localhost')
DB_PORT = os.environ.get('DB_PORT', '5432')
DB_NAME = os.environ.get('DB_NAME', 'testdb')
DB_USER = os.environ.get('DB_USER', 'testuser')
DB_PASS = os.environ.get('DB_PASS', 'testpass')

def get_connection():
    return psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASS
    )

def create_table():
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute('''CREATE TABLE IF NOT EXISTS test_table (
                id SERIAL PRIMARY KEY,
                name TEXT NOT NULL,
                value INTEGER
            )''')
            conn.commit()

def insert_row(name, value):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute('INSERT INTO test_table (name, value) VALUES (%s, %s) RETURNING id', (name, value))
            conn.commit()
            return cur.fetchone()[0]

def update_row(row_id, value):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute('UPDATE test_table SET value=%s WHERE id=%s', (value, row_id))
            conn.commit()

def delete_row(row_id):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute('DELETE FROM test_table WHERE id=%s', (row_id,))
            conn.commit()

def select_rows():
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute('SELECT id, name, value FROM test_table')
            return cur.fetchall()

if __name__ == "__main__":
    create_table()
    print("Table created and ready.")
