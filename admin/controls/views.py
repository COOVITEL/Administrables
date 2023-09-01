from django.shortcuts import render, redirect
from .models import TasasCDAT, TasasCooviahorro
from .forms import CreateUserForm, LoginForm

from django.contrib.auth.decorators import login_required

# Authetication models and functions

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout


def Index(request):
    return render(request, 'authentication/index.html')

# Register new user with the permissions
def Register(request):

    form = CreateUserForm()
    
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    
    context = {'registerform': form}

    return render(request, 'authentication/register.html', context=context)

# Login sesion with the users
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

# Close sesion
def user_logout(request):
    auth.logout(request)
    return redirect('index')

# Render the options controls
@login_required(login_url="login")
def Admin(request):
    return render(request, 'options.html')

# Return the all Cdats controls
@login_required(login_url="login")
def Cdat(request):
    cdats = TasasCDAT.objects.all()
    return render(request, 'cdat.html', {'cdats': cdats})

# Create new control cdat
def createCdat(request):
    if request.method == 'POST':
        since = request.POST['since']
        until = request.POST['until']
        amountsince = request.POST['amountsince']
        amountuntil = request.POST['amountuntil']
        tasa = request.POST['tasa']

        create = TasasCDAT(since=since, until=until, amountsince=amountsince, amountuntil=amountuntil, tasa=tasa)
        create.save()
        return redirect('cdats')
    return render(request, 'createcdat.html')

def updatecdat(request, id):
    cdat = TasasCDAT.objects.get(id=id)
    context = {"cdat": cdat}
    if request.method == 'POST':        
        cdat.since = request.POST['since']
        cdat.until = request.POST['until']
        cdat.amountsince = request.POST['amountsince']
        cdat.amountuntil = request.POST['amountuntil']
        cdat.tasa = request.POST['tasa']
        cdat.save()
        return redirect('cdats')
    return render(request, 'updatecdat.html', context)
        

# Return all Cooviahorros controls
@login_required(login_url="login")
def Cooviahorro(request):
    ahorros = TasasCooviahorro.objects.all()
    return render(request, 'ahorros.html', {'ahorros': ahorros})

def createCooviahorro(request):
    if request.method == 'POST':
        type = request.POST['type']
        amountMin = request.POST['amountMin']
        termMin = request.POST['termMin']
        tasa = request.POST['tasa']
        
        create = TasasCooviahorro(type=type, amountMin=amountMin, termMin=termMin, tasa=tasa)
        create.save()
        return redirect('cooviahorro')
    return render(request, 'createcooviahorro.html')

# Get cooviahorro
def updatecooviahorro(request, id):
    cooviahorro = TasasCooviahorro.objects.get(id=id)
    context = cooviahorro
    if request.method == 'POST':
        cooviahorro.amountMin = request.POST['amountMin']
        cooviahorro.termMin = request.POST['termMin']
        cooviahorro.tasa = request.POST['tasa']
        cooviahorro.save()
        return redirect('cooviahorro')      
    return render(request, 'updatecooviahorro.html', {'cooviahorro': context})