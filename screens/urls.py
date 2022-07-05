from django.urls import path
from . import views

from django.urls import include, re_path


urlpatterns=[
    path("", views.index),
    path("index", views.index),
    path('postsignIn/', views.postsignIn),
    path("ogrencigiris", views.ogrencigiris),
    path("ogrencikayit", views.ogrencikayit,name="kayit"),
    path('ogrencigiris', views.cikis, name="log"),
    path('postsignUp/', views.postsignUp),
    path("bursverenkayit", views.bursverenkayit),
    path("bursverengiris", views.bursverengiris),
    path("ogrenciform",views.ogrenciform),
    path("ogrenciprofil", views.ogrenciprofil),
    path("bursverenprofil", views.bursverenprofil),
    path("ilanlar", views.ilanlar),
    path("ilanekle", views.ilanekle),
    re_path(r'^postcreate', views.postcreate, name='postcreate')

]