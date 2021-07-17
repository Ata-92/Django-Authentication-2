from django.shortcuts import render, redirect, HttpResponse
from .forms import UserProfileForm, UserForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request, 'users/index.html')

def register(request):
    pass

def user_logout(request):
    pass

def user_login(request):
    pass

def studens(request):
    pass
