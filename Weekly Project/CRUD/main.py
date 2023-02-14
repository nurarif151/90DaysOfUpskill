from controllers.product_controller import ProductController

class Main:
    def __init__(self):
        self.controller = ProductController()

    def menu(self):
        print("\nWelcome to Product Management System")
        print("1. Create Product")
        print("2. Show Products")
        print("3. Update Product")
        print("4. Delete Product")
        print("0. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter product name: ")
            price = input("Enter product price: ")
            self.controller.create_product(name, price)
        elif choice == "2":
            self.controller.show_products()
        elif choice == "3":
            id = input("Enter product id: ")
            name = input("Enter product name: ")
            price = input("Enter product price: ")
            self.controller.update_product(id, name, price)
        elif choice == "4":
            id = input("Enter product id: ")
            self.controller.delete_product(id)
        elif choice == "0":
            print("Exiting...")
            exit()
        else:
            print("Invalid choice.")

    def run(self):
        while True:
            self.menu()

if __name__ == "__main__":
    main = Main()
    main.run()
