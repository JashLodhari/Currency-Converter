from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path,include
from home import views

urlpatterns = [
    path("", views.index, name='home'),
    path("unitconverter", views.unitconverter, name='unitconverter'),
    path("studentcorner", views.studentcorner, name='studentcorner'),
    path("search", views.search, name='search'),
    path("about", views.about, name='about'),
    path("contact", views.contact, name='contact'),
    path("length", views.length, name='length'),
    path("library", views.library, name='library'),
   path("speed", views.speed, name='speed'),
   path("temperature", views.temperature, name='temperature'),
   path("weight", views.weight, name='weight'),
   path("area", views.area, name='area'),
   path("time", views.time, name='time'),
   path("discount", views.discount, name='discount'),
   path("data", views.data, name='data'),
   path("mass", views.mass, name='mass'),
   path("age", views.age, name='age'),
   path("bmi", views.bmi, name='bmi'),
   path("pressure", views.pressure, name='pressure'),
   path("currencyconverter", views.currencyconverter, name='currencyconverter'),
]
''