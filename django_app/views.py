'''
ARQUIVO PARA DEFINIR OS TEMPLATES DA APLICAÇAO E OQ FAZEMOS COM ELES
'''
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.views import View

from .forms import UserRegistration, LoginForm
from .models import Users
from django.conf import settings
from . import forms


# DEFINIÇÃO VIEW DE LOGIN -- AINDA NÃO ESTÁ REDIRECIONANDO
class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'registration/login.html', {'form': form})
    def post(self, request):
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return render(request, 'home.html')
            else:
                form.add_error(None, "Nome de usuário ou senha incorretos")
        return render(request, 'registration/login.html', {'form': form})

# DEFINIÇÃO VIEW DE REGISTRO DO USUÁRIO E JA REDIRECIONANDO
def cadastro(request):
    if request.method == 'POST':
        form = UserRegistration(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'home.html')
    else:
        form = UserRegistration()
    return render(request, 'register.html', {'form': form})