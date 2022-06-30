from django.urls import path
from . import views


urlpatterns=[
    path("", views.index),
    path("index", views.index),
    path("ogrencigiris", views.ogrencigiris),
    path("ogrencikayit", views.ogrencikayit),
    path("bursverenkayit", views.bursverenkayit),
    path("bursverengiris", views.bursverengiris),
<<<<<<< HEAD
    path("ogrenciform",views.ogrenciform),
    path("profilim",views.ogrenciprofil),
=======
    path("profilim", views.ogrenciprofil),
    path("bursverenprofil", views.bursverenprofil),
    path("ilanlar", views.ilanlar),
    path("ilanekle", views.ilanekle),
>>>>>>> 06de4e2c68f2972a1e44b9514983e02f9043025b
]