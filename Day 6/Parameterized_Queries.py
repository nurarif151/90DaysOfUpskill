import mysql.connector

class Database:
    def __init__(self):
        self.host = "localhost"
        self.user = "phpmyadmin"
        self.password = "windows123"
        self.db = "tes"
        self.conn = None
        self.cursor = None

    def connect(self):
        self.conn = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.db
        )
        self.cursor = self.conn.cursor()

    def close(self):
        self.conn.commit()
        self.cursor.close()
        self.conn.close()

    def execute(self, sql, values=None):
        self.connect()
        if values:
            self.cursor.execute(sql, values)
        else:
            self.cursor.execute(sql)
        self.close()

    def fetchall(self, sql, values=None):
        self.connect()
        if values:
            self.cursor.execute(sql, values)
        else:
            self.cursor.execute(sql)
        result = self.cursor.fetchall()
        self.close()
        return result

    def fetchone(self, sql, values=None):
        self.connect()
        if values:
            self.cursor.execute(sql, values)
        else:
            self.cursor.execute(sql)
        result = self.cursor.fetchone()
        self.close()
        return result

db = Database()

# Insert data
sql = "INSERT INTO users (username, email) VALUES (%s, %s)"
values = ("user1", "user1@email.com")
db.execute(sql, values)

# Select all data
sql = "SELECT * FROM users"
result = db.fetchall(sql)
for row in result:
    print(row)

# Select single data
sql = "SELECT * FROM users WHERE id = %s"
values = (1,)
result = db.fetchone(sql, values)
print(result)

# Update data
sql = "UPDATE users SET username = %s WHERE id = %s"
values = ("updated_user", 1)
db.execute(sql, values)

# Delete data
sql = "DELETE FROM users WHERE id = %s"
values = (1,)
db.execute(sql, values)
