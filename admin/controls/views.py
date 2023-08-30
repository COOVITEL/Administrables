from django.shortcuts import render, redirect
from .models import TasasCDAT, TasasCooviahorro
from .forms import CreateUserForm, LoginForm

from django.contrib.auth.decorators import login_required

# Authetication models and functions

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout


def Index(request):
    return render(request, 'authentication/index.html')

def Register(request):

    form = CreateUserForm()
    
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    
    context = {'registerform': form}

    return render(request, 'authentication/register.html', context=context)

def login(request):
    
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                auth.login(request, user)
                
                return redirect("admin")
            
    context = {'loginform': form}
    
    return render(request, 'authentication/login.html', context=context)

def user_logout(request):
    auth.logout(request)
    return redirect('index')

@login_required(login_url="login")
def Admin(request):
    return render(request, 'options.html')

@login_required(login_url="login")
def Cdat(request):
    cdats = TasasCDAT.objects.all()
    return render(request, 'cdat.html', {'cdats': cdats})


@login_required(login_url="login")
def Cooviahorro(request):
    ahorros = TasasCooviahorro.objects.all()
    return render(request, 'ahorros.html', {'ahorros': ahorros})

