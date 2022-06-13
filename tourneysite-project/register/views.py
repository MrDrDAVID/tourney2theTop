from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate


# Create your views here.
def register(request) :
    if request.method == 'GET' :
        return render(request, 'register/register.html', {'form': UserCreationForm()})