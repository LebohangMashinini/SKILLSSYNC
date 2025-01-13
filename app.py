import pyrebase
import click
from dotenv import load_dotenv
import os

load_dotenv()
firebaseConfig = {
  'apiKey': os.getenv('APIKEY'),
  'authDomain': os.getenv('AUTHDOMAIN'),
  'projectId': os.getenv('PROJECTID'),
  'storageBucket': os.getenv('STORAGEBUCKET'),
  'messagingSenderId': os.getenv('MESSAGINGSENDERID'),
  'appId': os.getenv('APPID'),
  'measurementId': os.getenv('MEASUREMENTID'),
  'database_url': os.getenv('DATABASE_URL')
  }

firebase = pyrebase.Pyrebase(firebaseConfig)

auth=firebase.auth()
db = firebase.database()

print("Firebase Initialized successfully!")
