from django.shortcuts import redirect, render
from django.contrib.auth.hashers import make_password

def home(request):
    return render(request, 'home.html')
