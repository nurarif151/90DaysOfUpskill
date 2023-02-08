from Parameterized_Queries import Database

def menu():
    print("--- Database Menu ---")
    print("1. Insert data")
    print("2. Select all data")
    print("3. Select single data")
    print("4. Update data")
    print("5. Delete data")
    print("6. Exit")
    choice = int(input("Enter your choice: "))
    return choice

def insert_data():
    username = input("Enter username: ")
    email = input("Enter email: ")
    sql = "INSERT INTO users (username, email) VALUES (%s, %s)"
    values = (username, email)
    db.execute(sql, values)
    print("Data inserted successfully.")

def select_all_data():
    sql = "SELECT * FROM users"
    result = db.fetchall(sql)
    print("--- All Users ---")
    for row in result:
        print(row)

def select_single_data():
    id = int(input("Enter user id: "))
    sql = "SELECT * FROM users WHERE id = %s"
    values = (id,)
    result = db.fetchone(sql, values)
    print("--- User ---")
    print(result)

def update_data():
    id = int(input("Enter user id: "))
    username = input("Enter new username: ")
    sql = "UPDATE users SET username = %s WHERE id = %s"
    values = (username, id)
    db.execute(sql, values)
    print("Data updated successfully.")

def delete_data():
    id = int(input("Enter user id: "))
    sql = "DELETE FROM users WHERE id = %s"
    values = (id,)
    db.execute(sql, values)
    print("Data deleted successfully.")

db = Database()

while True:
    choice = menu()
    if choice == 1:
        insert_data()
    elif choice == 2:
        select_all_data()
    elif choice == 3:
        select_single_data()
    elif choice == 4:
        update_data()
    elif choice == 5:
        delete_data()
    elif choice == 6:
        print("Exiting...")
        break
    else:
        print("Invalid choice. Try again.")
