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
print(firebaseConfig)

firebase = pyrebase.initialize_app(firebaseConfig)

auth=firebase.auth()
db = firebase.database()

print("Firebase Initialized successfully!")

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
        print("User Response:", user)
        user_id = user["localId"]

        db.child("users").child(user_id).set({
            "name": name,
            "email": email,
            "role": role
        })
        click.echo("Account created account successfully!")
    except Exception as e:
        print("Error Details:", str(e))
        click.echo(f"Error: {e}")
        error_message = str(e)
        if "EMAIL_EXISTS" in error_message:
            click.echo("An account with this email already exists.")
        else:
            click.echo(f"Error: {e}")

def login():
    click.echo("Login...")
    email = input("Enter email: ")
    password = pwinput.pwinput("Enter your password: ")

    try:
        user = auth.sign_in_with_email_and_password(email, password)
        click.echo("Login successful!")
    except Exception as e:
        auth.get_account_info(password)
        click.echo("Incorrect password. Please try again.")

if __name__ == '__main__':
    signup()