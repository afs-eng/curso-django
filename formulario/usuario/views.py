from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .forms import LoginForm, SignupForm
from django.contrib import messages
from django.contrib.messages import constants


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
                messages.add_message(request, constants.SUCCESS, 'Login realizado com sucesso')
                return redirect('index')
        print(request.user)
        messages.add_message(request, constants.ERROR, 'Usuário ou senha inválidos')
    elif request.method == 'GET':
        form = LoginForm()
    return render(request, 'usuario/login.html', {'form': form})


def logout(request):
    logout(request)
    messages.add_message(request, constants.SUCCESS, 'Logout realizado com sucesso')
    return redirect('index')


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            confirmar_password = form.cleaned_data['confirmar_password']

            if password != confirmar_password:
                messages.add_message(request,constants.ERROR, 'As senhas não confere')
                return render(request, 'usuario/signup.html', {'form': form})
            elif User.objects.filter(username=username).exists():
                messages.add_message(request, constants.ERROR, 'Nome de usuario já existe')
                return render(request, 'usuario/signup.html', {'form': form})
            elif User.objects.filter(email=email).exists():
                messages.add_message(request, constants.ERROR, 'Email já cadastrado')
                return render(request, 'usuario/signup.html', {'form': form})

            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            messages.add_message(request, constants.SUCCESS, 'usuario criado com sucesso.')
            return redirect('login')
    else:

        form = SignupForm()

    return render(request, 'usuario/signup.html', {'form': form})
