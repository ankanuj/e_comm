from django.urls import path
from . import views

urlpatterns = [
	path('logout',views.logout,name='logout'),
	path('profile/',views.Profile,name='profile'),

]