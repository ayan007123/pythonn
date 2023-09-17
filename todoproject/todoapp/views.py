# from django.shortcuts import render
from django.urls import path
from .import views
from .import views
# Create your views here.
path('',views.add,name='add')
