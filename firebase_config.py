import pyrebase
import os
from dotenv import load_dotenv

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
auth = firebase.auth()
db = firebase.database()

print("Firebase Initialized successfully!")
