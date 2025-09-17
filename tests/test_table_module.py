import sqlite3
import pytest
from table_module import OrdersTable

@pytest.fixture
def setup_db():
    """Fixture to create in-memory DB with sample data"""
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE orders (id INTEGER, customer TEXT, total REAL)")
    cursor.executemany("INSERT INTO orders VALUES (?, ?, ?)", [
        (1, "Alice", 120.0),
        (2, "Bob", 80.5),
        (3, "Alice", 45.0)
    ])
    return conn

def test_total_sales(setup_db):
    orders = OrdersTable(setup_db)
    assert orders.total_sales() == pytest.approx(245.5)

def test_sales_by_customer_alice(setup_db):
    orders = OrdersTable(setup_db)
    assert orders.sales_by_customer("Alice") == pytest.approx(165.0)

def test_sales_by_customer_bob(setup_db):
    orders = OrdersTable(setup_db)
    assert orders.sales_by_customer("Bob") == pytest.approx(80.5)

def test_sales_by_customer_unknown(setup_db):
    orders = OrdersTable(setup_db)
    assert orders.sales_by_customer("Charlie") == 0.0
