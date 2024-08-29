from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .forms import LoginForm


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            print(f'name: {username} senha: {password}')
            user = auth.authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
                print(request.user)
                return redirect('index')
        print(request.user)
    elif request.method == 'GET':
        form = LoginForm()
    return render(request, 'usuario/login.html', {'form': form})


def logout(request):
    logout(request)
    return redirect('index')
