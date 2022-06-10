from multiprocessing import context
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User, Group
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from Company.models import *
from .form import CreateSuperUser
from django.contrib.auth.decorators import login_required
from django.core import validators
# Create your views here.


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user.groups.exists():
            a = user.groups.all()[0].name
            if a == 'Admin':
                login(request, user)
                return redirect('admin-dashbord',)
            elif a == 'Agent':
                login(request, user)
                return redirect('agent_dashbord')
            elif a == 'Customer':
                login(request, user)
                return redirect('Customer_dashbord')
            elif a == 'Financ_admin':
                login(request, user)
                return redirect('finance_admin_home')
            elif a == 'Store_Manager':
                login(request, user)
                return redirect('store-manager-home')
        else:
            return render(request, 'Account/login.html')
    return render(request, 'Account/login.html')


def logout_view(request):
    logout(request)
    return redirect('login')

# make crate super order

def SuperUser_CreateView(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        context ={
            'first_name':
        }

    return render(request, 'Account/Create_SuperUser_registration.html',)
