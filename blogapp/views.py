from django.shortcuts import render, HttpResponseRedirect
from .forms import Sign_Up_Forms, Login_Forms
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Post

# Create your views here.

# Home Base Functions ----
def home(request):
    posts = Post.objects.all()
    return render(request, 'blogapp/home.html',{'post':posts})

# About Base Functions ----
def about(request):
    return render(request, 'blogapp/about.html')

# About Base Functions ----
def contact(request):
    return render(request, 'blogapp/contact.html')

# Deshbord Base Functions ----
def deshbord(request):
    if request.user.is_authenticated:
        posts = Post.objects.all()
        return render(request, 'blogapp/deshbord.html',{'posts':posts})
    else:
        return HttpResponseRedirect('/login/')

# Deshbord Base Functions ----
def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm = Login_Forms(request=request, data=request.POST)
            if fm.is_valid():
                u_name = fm.cleaned_data['username']
                u_pass = fm.cleaned_data['password']
                user = authenticate(username= u_name, password= u_pass)
                if user is not None:
                    login(request,user)
                    messages.success(request,"Logged in Successfully !!")
                    return HttpResponseRedirect('/deshbord/')
        else:       
            fm = Login_Forms()
        return render(request, 'blogapp/login.html', {'form':fm})
    else:
        return HttpResponseRedirect('/deshbord/')
    
# Deshbord Base Functions ----
def user_signup(request):
    if request.method == 'POST':
        fm = Sign_Up_Forms(request.POST)
        if fm.is_valid():
            messages.success(request,"Thanks for signing up. Your account has been created !!")
            fm.save()
    else:
        fm = Sign_Up_Forms()
    return render(request, 'blogapp/signup.html', {'form': fm})

# Deshbord Base Functions ----
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')