import pyrebase
import click
from dotenv import load_dotenv
import os

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

def login():
    pass

@click.command()
@click.option('--email', prompt='Enter email', help='Your email address.')
@click.option('--password', prompt='Enter password', hide_input=True, help='Your password.')
def signup():
    email = input("Enter email: ")
    password = input("Enter your password: ")

    try:
        user = auth.password_email_exist(email, password)
    except:
        print("An account with this email already exist. Please use a different email")