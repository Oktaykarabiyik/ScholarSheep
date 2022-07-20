from distutils.command.config import config
import email
from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render
import pyrebase
from uuid import uuid4

from requests import session


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

id="123"
mail="sda"
password="1345"

firebase=pyrebase.initialize_app(config)
authe=firebase.auth()
database=firebase.database()
db = firebase.database()


def signIn(request):
    return render(request,"index.html")
def home(request):
    return render(request,"index.html")
 
def postsignIn(request):
    email=request.POST.get('email')
    pasw=request.POST.get('pass')
    try:
        # if there is no error then signin the user with given email and password
        user=authe.sign_in_with_email_and_password(email,pasw)
        uid = user['localId']
        request.session['logged_ogrenci_id'] = uid
        adsoyad = db.child("ogrenciler").child(uid).child("adsoyad").get().val()
        tel = db.child("ogrenciler").child(uid).child("telefon").get().val()
        okul = db.child("ogrenciler").child(uid).child("okuladi").get().val()
        adres = db.child("ogrenciler").child(uid).child("ikametgah").get().val()
        ad_soyadi=adsoyad
        tel_no=tel
        e_mail=email

        context = {

                'ad_soyadi': ad_soyadi,
                'e_mail':e_mail,
                'tel_no':tel_no,
                'okul':okul,
                'adres':adres,

             }
        print(ad_soyadi)
        print(tel_no)


        return render(request,"ogrenciprofil.html",context=context)
    except:
        message="Invalid Credentials!!Please ChecK your Data"
        return render(request,"ogrencigiris.html",{"message":message})
    session_id=user['idToken']
    request.session['uid']=str(session_id)
    

def cikis(request):
    try:
        request.session.flush()
        print("çıkış yapıldı")
    except Exception as e:
        print(e)
        pass
    return render(request,"ogrencigiris.html")
 
 
def postsignUp(request):
    email = request.POST.get('email')
    passs = request.POST.get('pass')
    password=passs
    adsoyad=request.POST.get('adsoyad')
    telefon=request.POST.get('telefon')
    yas=request.POST.get('yas')
    egitimduzeyi=request.POST.get('egitimduzeyi')
    okuladi=request.POST.get('okuladi')
    notortalama=request.POST.get('notortalama')
    aylikgelir=request.POST.get('aylikgelir')
    annesagdurumu=request.POST.get('annesagdurumu')
    babasagdurumu=request.POST.get('babasagdurumu')
    sehityakinlikdurumu=request.POST.get('sehityakinlikdurumu')
    ikametgah=request.POST.get('ikametgah')
    ad_soyadi=adsoyad
    tel_no=telefon
    okul=okuladi
    adres=ikametgah
    print(email)
    print(telefon)
    try:
        # creating a user with the given email and password
        if email is not None:
            print('Email Girdi')
            user=authe.create_user_with_email_and_password(email,passs)
            uid = user['localId']
            mail=user['email']
            print(uid)
            request.session['uid'] = uid
            request.session['email']=mail
        if 'uid' in request.session and adsoyad is not None:
            uid = request.session['uid']
            mail=request.session['email']
            e_mail=mail
            print(uid)
        
            data={
                "adsoyad":adsoyad,
                "telefon":telefon,
                "yas":yas,
                "egitimduzeyi":egitimduzeyi,
                "okuladi":okuladi,
                "notortalama":notortalama,
                "aylikgeir":aylikgelir,
                "annesagdurumu":annesagdurumu,
                "babasagdurumu":babasagdurumu,
                "sehityakinlikdurumu":sehityakinlikdurumu,
                "ikametgah":ikametgah        
            }
            database.child("ogrenciler").child(uid).set(data)
            context = {

                'ad_soyadi': ad_soyadi,
                'tel_no':tel_no,
                'e_mail':e_mail,
                'okul':okul,
                'adres':adres,

             }
        
    except Exception as e:
        print(e)
        return render(request, "ogrenciform.html") 
    
    print("merhaba3")
   
    if (adsoyad is not None):
        return render(request,"ogrenciprofil.html",context=context)
    else:
        return render(request,"ogrenciform.html")

    
def bursverensignIn(request):
    return render(request,"index.html")
 
def bursverenpostsignIn(request):
    email=request.POST.get('email')
    pasw=request.POST.get('pass')
    try:
        # if there is no error then signin the user with given email and password
        user=authe.sign_in_with_email_and_password(email,pasw)
        uid = user['localId']
        print(uid)
        adsoyad = db.child("bursverenler").child(uid).child("adsoyad").get().val()
        tel = db.child("bursverenler").child(uid).child("telefon").get().val()
        ad_soyadi=adsoyad
        tel_no=tel
        e_mail=email

        request.session['logged_email'] = email
        request.session['logged_passw'] = pasw
            
        context = {

                'ad_soyadi': ad_soyadi,
                'e_mail':e_mail,
                'tel_no':tel_no,
             }
        print(ad_soyadi)
        print(tel_no)
        return render(request,"bursverenprofil.html",context=context)

        
    except:
        message="Invalid Credentials!!Please ChecK your Data"
        print("hatali sifre")
        return render(request,"bursverengiris.html",{"message":message})
    session_id=user['idToken']
    request.session['uid']=str(session_id)
    
 
def bursverencikis(request):
    try:
        del request.session['uid']
    except:
        pass
    return render(request,"bursverengiris.html")
 
 
def bursverenpostsignUp(request):
     email = request.POST.get('email')
     passs = request.POST.get('pass')
     adsoyad=request.POST.get('adsoyad')
     tel=request.POST.get('telefon')
     try:
       if email is not None:
            print('Email Girdi')
            user=authe.create_user_with_email_and_password(email,passs)
            uid = user['localId']
            e_mail=user['email']
            print(uid)
            print(e_mail)
            request.session['uid'] = uid
            request.session['email']= e_mail
       if 'uid' in request.session and adsoyad is not None:
            uid = request.session['uid']
            e_mail=request.session['email']
            print(uid)
            ad_soyadi=adsoyad
            tel_no=tel
            data={
                "adsoyad":adsoyad,
                "tel":tel,        
                 }

            database.child("bursverenler").child(uid).set(data)

            context = {

                'ad_soyadi': ad_soyadi,
                'tel_no':tel_no,
                'e_mail':e_mail,
             }
     except:
        return render(request, "bursverenkayit.html")
     if (adsoyad is not None):
        return render(request,"bursverenprofil.html",context=context)
     else:
        return render(request,"bursverenform.html")

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

    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'ilanbasvur':
            ilanid = request.POST.get('ilanId')
            ogrenciid = request.session['logged_ogrenci_id']
            print(ilanid)
            print(ogrenciid)
            if ilanid is not None:
                try:
                    basvuranlar = db.child("ilanlar").child(ilanid).child("basvuranlarID").get().val()
                    ogrenciyok = True
                    for elem in basvuranlar:
                        if elem == ogrenciid:
                            ogrenciyok = False
                    print(basvuranlar)
                    if ogrenciyok:
                        basvuranlar.append(ogrenciid)
                        db.child("ilanlar").child(ilanid).child("basvuranlarID").set(basvuranlar)
                except Exception as e:
                    print(e)

    ilanlar = db.child("ilanlar").get().val()
    for d1 in ilanlar:
        print(ilanlar[d1].get('bursverenid'))
        
    ilan_list = []
    for elem in ilanlar:
        ilan = {
            'bursAdi':ilanlar[elem].get('bursad'),
            'aciklama':ilanlar[elem].get('aciklama'),
            'bursmiktari':ilanlar[elem].get('bursmiktari'),
            'sonbasvurutarihi':ilanlar[elem].get('sonbasvurutarihi'),
            'ilanid':ilanlar[elem].get('ilanID')
            }
        ilan_list.append(ilan)
    context={
        'ilan_list':ilan_list
    }
    return render(request,"ilanlar.html",context=context)

def basvuranlarlist(request):
    
    
    
    return

def basvuruyap(request,ilanID):
    email = request.session['logged_email']
    passs = request.session['logged_passw']

    user=authe.sign_in_with_email_and_password(email,passs)
    uid = user['localId']    
    ilanID = request.POST.get('ilanID')

    data={                
                "basvuranlarID":["uid"],                    
        }
    database.child("ilanlar").child(ilanID).set(data)

    return render(request,"ilanlar.html")

def ilanekle(request):
    bursadi = request.POST.get('bursad')
    bursmiktari = request.POST.get('bursmiktari')
    aciklama=request.POST.get('aciklama')
    sonbasvurutarihi=request.POST.get('sonbasvurutarihi')
    email = request.session['logged_email']
    passs = request.session['logged_passw']

    try:
        # if there is no error then signin the user with given email and password
        user=authe.sign_in_with_email_and_password(email,passs)
        print("gecti")
        uid = user['localId']
        print(uid)
        print("gecti2")
        data={
                "aciklama":aciklama,
                "bursad":bursadi,
                "bursmiktari":bursmiktari,
                "bursverenid":uid,
                "sonbasvurutarihi":sonbasvurutarihi,
                "basvuranlarID":[""]
                       
        }
         
        unique_id = str(uuid4())
        if bursadi is not None:
            database.child("ilanlar").child(unique_id).set(data)

    except Exception as e:
        print(e)
        message="Invalid Credentials!!Please ChecK your Data"

    return render(request,"ilanekle.html")

def basvuranlar(request):
    return render(request,"basvuranlar.html")
def bursverenform(request):
    return render(request,"bursverenform.html")
