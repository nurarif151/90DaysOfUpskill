import sqlite3

class ProductController:
    def __init__(self):
        self.conn = sqlite3.connect('products.db')
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        query = '''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            price REAL NOT NULL
        );
        '''
        self.cursor.execute(query)
        self.conn.commit()

    def create_product(self, name, price):
        query = "INSERT INTO products (name, price) VALUES (?, ?)"
        self.cursor.execute(query, (name, price))
        self.conn.commit()
        print("Product created successfully.")

    def show_products(self):
        query = "SELECT * FROM products"
        self.cursor.execute(query)
        products = self.cursor.fetchall()
        print("ID\tName\t\tPrice")
        print("-"*25)
        for product in products:
            print("{}\t{}\t\t{}".format(product[0], product[1], product[2]))

    def update_product(self, id, name, price):
        query = "UPDATE products SET name=?, price=? WHERE id=?"
        self.cursor.execute(query, (name, price, id))
        self.conn.commit()
        print("Product updated successfully.")

    def delete_product(self, id):
        query = "DELETE FROM products WHERE id=?"
        self.cursor.execute(query, (id,))
        self.conn.commit()
        print("Product deleted successfully.")
