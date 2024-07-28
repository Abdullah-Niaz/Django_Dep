from django.http import HttpResponse
from django.shortcuts import render
from django.urls import path

def home(request):
    return render(request,'base.html')