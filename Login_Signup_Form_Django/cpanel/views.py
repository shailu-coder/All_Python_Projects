#The Tann Mann Gaadi
#Python Assignment
#starting time - 9 apr 21- 5:30 PM

from django.shortcuts import render
import pyrebase
from django.contrib import auth

config = {
    "apiKey": "AIzaSyCN1YIT5aLeW41CAymG06ZnVEV-5KnVQa0",
    "authDomain": "cpanel-c8de1.firebaseapp.com",
    "projectId": "cpanel-c8de1",
    "storageBucket": "cpanel-c8de1.appspot.com",
    "messagingSenderId": "401803109923",
    "appId": "1:401803109923:web:edb5f2b450f64a014c7396",
    "measurementId": "G-Q78MRS55XR",
    "databaseURL" : "",
  }

firebase = pyrebase.initialize_app(config)

authe = firebase.auth()
database= firebase.database()


def singIn(request):
    return render(request, "SignIn.html")

def postsign(request):
    email = request.POST.get('email')
    passw = request.POST.get('pass')

    try:
      user = authe.sign_in_with_email_and_password(email, passw)
    except:
      message = "Invalid Credentials"
      return render(request, "SignIn.html", {"messg":message})

    # print(user['idToken'])

    session_id = user['idToken']
    request.session['uid'] = str(session_id)


    return render(request, "welcome.html", {"e":email})

def logout(request):
      auth.logout(request)
      return render (request, "SignIn.html")

def signup(request):
      return render (request, "signup.html")

def postsignup(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    passw = request.POST.get('pass')

    user = authe.create_user_with_email_and_password(email, passw)

    return render(request,"SignIn.html")


#Finishing Time - 10  Apr 21 - 9:30 AM
