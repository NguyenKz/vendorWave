from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import SignUpForm, SignInForm

def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return render(request, 'sign_up.html', {'form': form})#redirect('home')  # Redirect to your home page
    else:
        form = SignUpForm()
    return render(request, 'sign_up.html', {'form': form})

def sign_in(request):
    if request.method == 'POST':
        form = SignInForm(request, request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('/')  # Redirect to your home page
    else:
        form = SignInForm()
    return render(request, 'sign_in.html', {'form': form})