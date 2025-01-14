import pyrebase
import click
from dotenv import load_dotenv
import os
import pwinput

load_dotenv()
firebaseConfig = {
  'apiKey': os.getenv('APIKEY'),
  'authDomain': os.getenv('AUTHDOMAIN'),
  'projectId': os.getenv('PROJECTID'),
  'databaseURL': os.getenv('DATABASE_URL'),
  'storageBucket': os.getenv('STORAGEBUCKET'),
  'messagingSenderId': os.getenv('MESSAGINGSENDERID'),
  'appId': os.getenv('APPID'),
  'measurementId': os.getenv('MEASUREMENTID'),
  }

firebase = pyrebase.initialize_app(firebaseConfig)

auth=firebase.auth()
db = firebase.database()

print("Firebase Initialized successfully!")

def signup():
    click.echo("Signup...")
    email = input("Enter email: ")
    password = pwinput.pwinput("Enter your password: ")

    try:
        # Check if user exists
        auth.get_account_info(email)
        click.echo("An account with this email already exists.")
    except:
        try:
            # Create a new user
            user = auth.create_user_with_email_and_password(email, password)
            click.echo("Created account successfully!")
        except Exception as e:
            click.echo(f"Error: {e}")

def login():
    click.echo("Login...")
    email = input("Enter email: ")
    password = pwinput.pwinput("Enter your password: ")

    try:
        auth.get_account_info(password)
        click.echo("Incorrect password. Please try again.")
    except:
        try:
            # Create a new user
            login = auth.sign_in_with_email_and_password(email, password)
            click.echo("Login successful!")
        except Exception as e:
            click.echo(f"Error: {e}")

if __name__ == "__main__":
    signup()