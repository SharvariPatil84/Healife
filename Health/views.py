from django.shortcuts import render, HttpResponseRedirect
from .forms import SignUpForm

# Create your views here.
# Home
def home(request):
  return render(request, 'Health/home.html')
# About
def about(request):
  return render(request, 'Health/about.html')

# Contact
def contact(request):
  return render(request, 'Health/contact.html')

# Services
def services(request):
  return render(request, 'Health/services.html')

# Logout
def user_logout(request):
  return HttpResponseRedirect('/')

#Signup
def user_signup(request):
 form = SignUpForm()
 return render(request, 'Health/signup.html', {'form':form})

#Login
def user_login(request):
  return render(request, 'Health/login.html')