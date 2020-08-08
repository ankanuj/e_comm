from django.shortcuts import render, redirect
from django.contrib import messages,auth
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from cart.models import Address



@login_required(login_url='index')
def logout(request):
	if request.method == 'POST':
		auth.logout(request)
		return redirect('index')

@login_required
def Profile(request):
	user = User.objects.all().get(username=request.user.username)
	adds = Address.objects.all().get(user_id=request.user.id)
	content = {
		'user':user,
		'adds':adds
	}
	return render(request,'accounts/profile.html',content)