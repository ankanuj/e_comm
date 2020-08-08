from django.shortcuts import render,redirect
from django.contrib import messages,auth
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import Feedback

def index(request):
    if request.method == 'POST': 
        email = request.POST['email']
        comment = request.POST['feedback']
        feedback = Feedback(email=email, comment=comment)
        feedback.save()
    return render(request,'home_pages/index.html')

def about(request):
    return render(request,'home_pages/about.html')