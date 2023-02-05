import sqlite3

def create_sales_table():
    conn = sqlite3.connect("sales.db")
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS sales (date TEXT PRIMARY KEY, sales REAL)")
    conn.commit()
    conn.close()

def add_sales_data(date, sales):
    conn = sqlite3.connect("sales.db")
    c = conn.cursor()
    c.execute("INSERT INTO sales (date, sales) VALUES (?, ?)", (date, sales))
    conn.commit()
    conn.close()

def read_sales_data():
    conn = sqlite3.connect("sales.db")
    c = conn.cursor()
    c.execute("SELECT * FROM sales")
    data = c.fetchall()
    conn.close()
    return data

def update_sales_data(date, sales):
    conn = sqlite3.connect("sales.db")
    c = conn.cursor()
    c.execute("UPDATE sales SET sales=? WHERE date=?", (sales, date))
    conn.commit()
    conn.close()

def delete_sales_data(date):
    conn = sqlite3.connect("sales.db")
    c = conn.cursor()
    c.execute("DELETE FROM sales WHERE date=?", (date,))
    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_sales_table()
