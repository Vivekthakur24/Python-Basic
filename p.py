def register():
    username = input("Enter a username: ")
    password = input("Enter a password: ")
    users[username] = password4
    print("Registration successful!")

def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if username in users and users[username] == password:
        print("Login successful!")
    else:
        print("Invalid username or password.")

users = {}

while True:
    print("\nSelect an option:")
    print("1. Register")
    print("2. Login")
    print("3. Quit")
    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        register()
    elif choice == '2':
        login()
    elif choice == '3':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please enter 1 , 2, or 3.")