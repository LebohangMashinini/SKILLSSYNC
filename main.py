import click
from signup import signup
from login import login
from booking_system import booking

def main():
    click.echo("Firebase Initialized successfully!")
    click.echo("Choose an option:")
    click.echo("1. Signup")
    click.echo("2. Login")
    click.echo("3. Exit")

    choice = input("Enter your choice: ")

    user = None
    if choice == "1":
        user = signup()
    elif choice == "2":
        user = login()
    elif choice == "3":
        click.echo("Exiting...")
        return
    else:
        click.echo("Invalid choice. Try again.")
        main()

    if user:
        booking(user)

if __name__ == "__main__":
    main()

