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
    form_user = UserForm(request.POST or None)
    form_profile = UserProfileForm(request.POST or None)
    if form_user.is_valid() and form_profile.is_valid():
        user = form_user.save()
        # if you don't use ModelForm, you need to get values
        # --------------------------------------------------
        # username = form_user.cleaned_data.get('username')
        # password = form_user.cleaned_data.get('password')
        # email = form_user.cleaned_data.get('email')
        # if you don't use UserCreationForm, you need to save db
        # ------------------------------------------------------
        # user = User(username=username, email=email)
        # if you send password to class directly like above, it will not hash pasword
        # to save password encrypted use the command below
        # user.set_password(password)
        # user.save()
        profile = form_profile.save(commit=False)
        profile.user = user
        if 'profile_pic' in request.FILES:
            profile.profile_pic = request.FILES['profile_pic']
        profile.save()
        messages.success(request, "Register successful")
        return redirect('index')
    context = {
        'form_profile': form_profile,
        'form_user': form_user
    }
    return render(request, 'users/register.html', context)

def user_logout(request):
    pass

def user_login(request):
    pass

def studens(request):
    pass
