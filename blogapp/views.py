from django.shortcuts import render, HttpResponseRedirect
from .forms import Sign_Up_Forms

# Create your views here.

# Home Base Functions ----
def home(request):
    return render(request,'blogapp/home.html')

# About Base Functions ----
def about(request):
    return render(request,'blogapp/about.html')

# About Base Functions ----
def contact(request):
    return render(request,'blogapp/contact.html')

# Deshbord Base Functions ----
def deshbord(request):
    return render(request,'blogapp/deshbord.html')

# Deshbord Base Functions ----
def user_login(request):
    return render(request,'blogapp/login.html')

# Deshbord Base Functions ----
def user_signup(request):
    fm = Sign_Up_Forms()
    return render(request,'blogapp/signup.html',{'form': fm})

# Deshbord Base Functions ----
def user_logout(request):
    return HttpResponseRedirect('/')