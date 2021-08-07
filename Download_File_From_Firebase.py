import pyrebase
import time

config = {
    "apiKey": "AIzaSyDJkMyTuiXY1YlLYAu0aErRpRzD_QemzAw",
    "authDomain": "fileupdown-cc601.firebaseapp.com",
    "databaseURL": "https://fileupdown-cc601.firebaseio.com",
    "projectId": "fileupdown-cc601",
    "storageBucket": "fileupdown-cc601.appspot.com",
    "messagingSenderId": "492138959928",
    "appId": "1:492138959928:web:49db23b344d05026af82cd",
    "measurementId": "G-669K23RC8S"
  }

firebase = pyrebase.initialize_app(config)

storage = firebase.storage()

path_on_cloud="xyz.jpg" 
# location on cloud
# location on local drive/PC

def down():
    storage.child(path_on_cloud).download("C:","Down.jpg")


while True:
    down()
    time.sleep(60)
