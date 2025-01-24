import click
import pwinput
from firebase_config import auth

def login():
    click.echo("Login...")
    email = input("Enter email: ")
    password = pwinput.pwinput("Enter your password: ")

    try:
        user = auth.sign_in_with_email_and_password(email, password)
        click.echo("Login successful!")
    except Exception as e:
        if "INVALID_PASSWORD" in str(e):
            click.echo("Incorrect password. Please try again.")
        else:
            click.echo(f"Error: {e}")
