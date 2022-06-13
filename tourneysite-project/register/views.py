from django.shortcuts import render, redirect
from django.db import IntegrityError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate


# Create your views here.
def register(request) :
    if request.method == 'GET' :
        return render(request, 'register/register.html', {'form': UserCreationForm()})
    else :
        if request.POST['password1'] == request.POST['password2'] :
            try :
                user = User.objects.create_user(request.POST['username'],
                    password=request.POST['password1'])
                user.save() 
                login(request, user)

                return redirect('dashboard')
            except IntegrityError :
                return render(request, 'register/register.html', 
                {'form': UserCreationForm(), 'error': 'That username is taken'})
        else :
            return render(request, 'register/register.html', 
            {'form': UserCreationForm(), 'error': 'Passwords dont match'})

    def user_login(request) :
        if request.method == 'GET' :
            return render(request, 'register/login_user.html', 
            {'form': AuthenticationForm()})
        else :
            user = authenticate(request, username=request.POST['username'], 
            password=request.POST['password'])
            if user is None :
                return render(request, 'register/login_user.html', 
                {'form': AuthenticationForm(), 'error': 'Username and password did not match'})
            else :
                login(request, user)

                return redirect('dashboard')