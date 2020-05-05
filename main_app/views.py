from django.shortcuts import render,redirect
from django.contrib import messages,auth
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


def index(request):
	return render(request,'home_pages/index.html')

def about(request):
    return render(request,'home_pages/about.html')