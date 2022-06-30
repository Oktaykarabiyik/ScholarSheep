from distutils.command.config import config
from django.http import HttpResponse
from django.shortcuts import render
import pyrebase


config={
  "apiKey": "AIzaSyBmM91bv9cLoRFOYHO-0k9jBv9aN3Lhh8o",
  "authDomain": "scholarsheep-8fbec.firebaseapp.com",
  "projectId": "scholarsheep-8fbec",
  "databaseURL": "https://scholarsheep-8fbec-default-rtdb.firebaseio.com",
  "storageBucket": "scholarsheep-8fbec.appspot.com",
  "messagingSenderId": "177314107895",
  "appId": "1:177314107895:web:4e7164bbb31e683d38def2",
  "measurementId": "G-ETXWFENSN7"
}

firebase=pyrebase.initialize_app(config)
authe=firebase.auth()
database=firebase.database()

name=database.child('Ogrenciler').child('e_mail').get().val()
print(name)



def index(request):
    return render(request,"index.html")

def ogrencigiris(request):
    return render(request,"ogrencigiris.html")

def bursverengiris(request):
    return render(request,"bursverengiris.html")

def ogrencikayit(request):
    return render(request,"ogrencikayit.html")

def bursverenkayit(request):
    return render(request,"bursverenkayit.html")

def ogrenciform(request):
    return render(request,"ogrenciform.html")

def ogrenciprofil(request):
    return render(request,"ogrenciprofil.html")

def bursverenprofil(request):
    return render(request,"bursverenprofil.html")

def ilanlar(request):
    return render(request,"ilanlar.html")

def ilanekle(request):
    return render(request,"ilanekle.html")
