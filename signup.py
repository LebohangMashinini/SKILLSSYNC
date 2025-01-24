import click
import pwinput
from firebase_config import auth, db


def signup():
    click.echo("Signup...")
    email = input("Enter email: ")
    password = pwinput.pwinput("Enter your password: ")
    name = input("Enter your name: ")
    role = input("What is your role (mentor/peer): ")

    if role not in ["mentor", "peer"]:
        click.echo("Invalid input. Please enter 'mentor' or 'peer'.")
        return

    try:
        user = auth.create_user_with_email_and_password(email, password)
        user_id = user["localId"]
        auth_token = user["idToken"]

        db.child("users").child(user_id).set({
            "name": name,
            "email": email,
            "role": role
        }, auth_token)
        print("User added to database successfully!")
    except Exception as e:
        click.echo(f"Error: {e}")
        if "EMAIL_EXISTS" in str(e):
            click.echo("An account with this email already exists.")