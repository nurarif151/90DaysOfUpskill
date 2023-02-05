class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.is_logged_in = False

    def login(self, entered_username, entered_password):
        if entered_username == self.username and entered_password == self.password:
            self.is_logged_in = True
            return True
        return False

    def logout(self):
        self.is_logged_in = False


class UserManager:
    def __init__(self):
        self.users = []

    def register(self, username, password):
        user = User(username, password)
        self.users.append(user)

    def login(self, username, password):
        for user in self.users:
            if user.login(username, password):
                return user
        return None


user_manager = UserManager()


def register():
    print("Register")
    print("--------")
    username = input("Enter username: ")
    password = input("Enter password: ")
    user_manager.register(username, password)
    print("Successfully registered.")


def login():
    print("Login")
    print("-----")
    username = input("Enter username: ")
    password = input("Enter password: ")
    user = user_manager.login(username, password)
    if user:
        print("Successfully logged in.")
        user.is_logged_in = True
    else:
        print("Login failed.")


def logout(user):
    user.logout()
    print("Successfully logged out.")


def show_menu():
    print("Menu")
    print("----")
    print("1. Register")
    print("2. Login")
    print("3. Logout")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        register()
    elif choice == 2:
        login()
    elif choice == 3:
        logout(user)
    elif choice == 4:
        exit()


while True:
    show_menu()
