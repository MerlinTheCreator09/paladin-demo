"""Customer lookups. INTENTIONALLY INSECURE: SQL is built from strings."""
import sqlite3

DB_PATH = "data/demo.sqlite"


def find_customer(cid: str) -> dict:
    conn = sqlite3.connect(DB_PATH)
    row = conn.execute(f"SELECT id, name, email FROM customers WHERE id = '{cid}'").fetchone()
    return {"id": row[0], "name": row[1], "email": row[2]} if row else {}


def search(name: str) -> list:
    conn = sqlite3.connect(DB_PATH)
    return conn.execute("SELECT id, name FROM customers WHERE name LIKE '%" + name + "%'").fetchall()
