from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.


def user_profile(request):
    return render(request,'account/profile.html')


def home_page(request):
    return render(request,'account/home.html')


def register(request):
    return render(request, 'registration/register.html')