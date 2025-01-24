import click
from signup import signup
from login import login

def main():
    print("Firebase Initialized successfully!")
    print("Choose an option:")
    print("1. Signup")
    print("2. Login")
    choice = input("Enter your choice: ")

    if choice == "1":
        signup()
    elif choice == "2":
        login()
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()

