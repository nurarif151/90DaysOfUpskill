import database

def display_data_as_table(data):
    print("{:<10} {:<10}".format("Date", "Sales"))
    for d in data:
        print("{:<10} {:<10}".format(d[0], d[1]))

def show_sales_data():
    data = database.read_sales_data()
    display_data_as_table(data)

def add_sales():
    date = input("Enter date (YYYY-MM-DD): ")
    sales = float(input("Enter sales: "))
    database.add_sales_data(date, sales)
    print("Data added successfully")

def update_sales():
    date = input("Enter date (YYYY-MM-DD) to update: ")
    sales = float(input("Enter updated sales: "))
    database.update_sales_data(date, sales)
    print("Data updated successfully")

def delete_sales():
    date = input("Enter date (YYYY-MM-DD) to delete: ")
    database.delete_sales_data(date)
    print("Data deleted successfully")

if __name__ == '__main__':
    while True:
        print("1. Show sales data")
        print("2. Add sales data")
        print("3. Update sales data")
        print("4. Delete sales data")
        print("5. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            show_sales_data()
        elif choice == 2:
            add_sales()
        elif choice == 3:
            update_sales()
        elif choice == 4:
            delete_sales()
        elif choice == 5:
            break
        else:
            print("Invalid choice. Try again")
