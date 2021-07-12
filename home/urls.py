from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact', views.contact, name='contact'),
    path('aboutus', views.aboutus,name='aboutus'),
    path('search', views.search,name='search')

]

