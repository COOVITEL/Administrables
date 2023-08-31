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
        redirect('cdats')
    return render(request, 'createcdat.html')

# Get cdat
def getcdat(request, id):
    cdat = TasasCDAT.objects.get(id=id)
    return render(request, 'getcdat.html', {"cdat": cdat})

# Update cdat
def updatecdat(request, id):
    if request.method == 'POST':
        cdat = TasasCDAT.objects.get(id=id)
        cdat.since = request.PUT['since']
        cdat.until = request.PUT['until']
        cdat.amountsince = request.PUT['amountsince']
        cdat.amountuntil = request.PUT['amountuntil']
        cdat.tasa = request.PUT['tasa']

        cdat.save()
        redirect('cdats')
    return render(request, 'getcdat.html')

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
        redirect('cooviahorro')
    return render(request, 'createcooviahorro.html')

# Get cooviahorro
def getcooviahorro(request, id):
    cooviahorro = TasasCooviahorro.objects.get(id=id)
    return render(request, 'getcooviahorro.html', {'cooviahorro': cooviahorro})