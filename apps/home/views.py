from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

@login_required
def user_info(request):
    return render(request, 'user_info.html')