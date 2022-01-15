from django.shortcuts import render, redirect
from django.contrib import messages
# from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required


# def register(request):
#         form = UserCreationForm()
#         return render(request, 'users/register.html', {'form': form})

from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm



@login_required
def profile(request):
    return render(request, 'users/profile.html')


# Create your views here.
