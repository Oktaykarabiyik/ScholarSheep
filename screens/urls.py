from django.urls import path
from . import views

from django.urls import include, re_path


urlpatterns=[
    path("", views.index),
    path("index", views.index),
    path("ogrencigiris", views.ogrencigiris),
    path("ogrencikayit", views.ogrencikayit),
    path("bursverenkayit", views.bursverenkayit),
    path("bursverengiris", views.bursverengiris),
    path("profilim", views.ogrenciprofil),
    path("bursverenprofil", views.bursverenprofil),
    path("ilanlar", views.ilanlar),
    path("ilanekle", views.ilanekle),
    path("bursverenform", views.bursverenform),
    re_path(r'^postcreatetwo', views.postcreatetwo, name='postcreatetwo')
    
]