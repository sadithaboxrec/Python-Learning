


users={}

def main():
    print("Hello, Welcome to the Application")
    print("1.Login")
    print("2.Register")
    print("3.Exit")

    while True:
        user_choice = input("Enter your choice: ")

        match user_choice:
            case "1":
                login()
            case "2":
                register()
            case "3":
                exit()
            case _:
                print("Please enter a correct letter.\n")
                continue

def register():
    print("Welcome to the Application")

    while True:

        user_name = input("Enter your name: ")

        if user_name == "":
            print("Please enter a correct name.\n")
            continue
        elif user_name in users:
            print("That username has already registerd in.\n")
            continue
        else:
            password_verifier(user_name)





def password_verifier(user_name):

    while True:

        password = input("Enter your password: ")

        is_long=len(password) < 8
        has_uper_letters=any(char.isupper() for char in password)
        has_number=any(char.isdigit() for char in password)
        has_special=any(not char.isalnum() for char in password)

        if is_long and has_uper_letters and has_number and has_special:
            password_encrypt()


def password_encrypt():
    pass



def login():
    print("Welcome to the Application. Please enter your username and password.\n")

if __name__ == '__main__':
    main()






import hashlib

# -----------------------------------------
# Helper functions
# -----------------------------------------

def hash_password(password: str) -> str:
    """Return a SHA-256 hash of the password."""
    return hashlib.sha256(password.encode()).hexdigest()


# In-memory storage (volatil—erased when program ends)
users = {}


def register():
    print("\n--- Register ---")
    username = input("Enter new username: ")

    if username in users:
        print("Username already exists.\n")
        return

    password = input("Enter password: ")
    users[username] = hash_password(password)
    print("Registration successful!\n")


def login():
    print("\n--- Login ---")
    username = input("Username: ")

    if username not in users:
        print("User not found.\n")
        return

    password = input("Password: ")
    if users[username] == hash_password(password):
        print("Login successful!\n")
    else:
        print("Incorrect password.\n")


# -----------------------------------------
# Main menu loop
# -----------------------------------------

def main():
    while True:
        print("=== Login System ===")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            register()
        elif choice == "2":
            login()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.\n")


if __name__ == "__main__":
    main()
