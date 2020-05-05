from django.shortcuts import render, redirect
from django.contrib import messages,auth
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

def login(request):
	if request.method=='POST':
		
		username = request.POST['username']
		password = request.POST['password']
	
		user = auth.authenticate(request, username=username, password=password)
		
		if user is not None:

			auth.login(request,user)
			messages.success(request,'successfully Login')
			return redirect('index')
		else:
			messages.error(request,'password or username is not matched')
			return redirect('login')
		
		
	else:
		return render(request,'register/login.html')

def signup(request):
	if request.method == 'POST':
		username = request.POST['username']
		first_name = request.POST['first_name']
		last_name = request.POST['last_name']
		email = request.POST['email']
		password = request.POST['password']

		c_password = request.POST['c_password']
		
		if password == c_password:
			#check user name
			if User.objects.filter(username=username).exists():
				messages.error(request,'That username is taken')
				return redirect('signup')
			else:
				user = User.objects.create_user(username=username,first_name = first_name, last_name = last_name, email = email, password=password)
				user.save()
				messages.success(request,'Successfully registered now login')
				return redirect('login')

		else:
			messages.error(request,'Password not matched')
			return redirect('signup')
		
	else:
		return render(request,'register/signup.html')

		





