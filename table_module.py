import sqlite3

class OrdersTable:
    def __init__(self, connection):
        self.conn = connection

    def total_sales(self):
        """Return total sales from all orders"""
        cursor = self.conn.cursor()
        cursor.execute("SELECT SUM(total) FROM orders")
        return cursor.fetchone()[0] or 0.0

    def sales_by_customer(self, customer):
        """Return total sales for a given customer"""
        cursor = self.conn.cursor()
        cursor.execute("SELECT SUM(total) FROM orders WHERE customer=?", (customer,))
        return cursor.fetchone()[0] or 0.0


if __name__ == "__main__":
    # Demo in-memory DB
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE orders (id INTEGER, customer TEXT, total REAL)")
    cursor.executemany("INSERT INTO orders VALUES (?, ?, ?)", [
        (1, "Alice", 120.0),
        (2, "Bob", 80.5),
        (3, "Alice", 45.0)
    ])

    orders = OrdersTable(conn)
    print("💰 Total Sales:", orders.total_sales())
    print("🛒 Alice Sales:", orders.sales_by_customer("Alice"))
