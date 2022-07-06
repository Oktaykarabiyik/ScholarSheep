
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def postcreatetwo(request):

    adsoyad=request.POST.get('adsoyad')
    email=request.POST.get('email')
    tel=request.POST.get('tel')
    ikametgah=request.POST.get('ikametgah')

    data={
        "adsoyad":adsoyad,
        "email":email,
        "tel":tel,
        "ikametgah":ikametgah        
    }

    unique_id = str(uuid4())
    database.child("bursverenler").child(unique_id).set(data)

    return render(request, "bursverenprofil.html")

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
    
def ogrenciprofil(request):
    return render(request,"ogrenciprofil.html")

def bursverenprofil(request):
    return render(request,"bursverenprofil.html")

def ilanlar(request):
    return render(request,"ilanlar.html")

def ilanekle(request):
    return render(request,"ilanekle.html")

def bursverenform(request):
    return render(request,"bursverenform.html")
