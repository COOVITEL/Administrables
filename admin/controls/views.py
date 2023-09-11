from django.shortcuts import render, redirect
from .models import TasasCDAT, TasasCooviahorro
from .forms import CreateUserForm, LoginForm
from rest_framework import viewsets
from .serializer import CdatSerializer, CooviahorroSerializer

from django.contrib.auth.decorators import login_required

# Authetication models and functions

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout

# Login sesion with the users
def login(request):
    
    form1 = LoginForm()
    if request.method == 'POST':
        form1 = LoginForm(request, data=request.POST)
        if form1.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                auth.login(request, user)
                
                return redirect("admin")


    form2 = CreateUserForm() 
    if request.method == "POST":
        form2 = CreateUserForm(request.POST)
        if form2.is_valid():
            form2.save()
            return redirect('login')
    
    context = {'loginform': form1,
               'registerform': form2}
    
    return render(request, 'authentication/login.html', context=context)

# Close sesion
def user_logout(request):
    auth.logout(request)
    return redirect('login')

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
        type = request.POST['type']
        since = request.POST['since']
        until = request.POST['until']
        amountsince = request.POST['amountsince']
        amountuntil = request.POST['amountuntil']
        tasa = request.POST['tasa']

        create = TasasCDAT(type=type, since=since, until=until, amountsince=amountsince, amountuntil=amountuntil, tasa=tasa)
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

def deletecdat(request, id):
    cdat = TasasCDAT.objects.get(id=id)
    cdat.delete()
    return redirect('cdats')
        

# Return all Cooviahorros controls
@login_required(login_url="login")
def Cooviahorro(request):
    ahorros = TasasCooviahorro.objects.all()
    return render(request, 'cooviahorro.html', {'ahorros': ahorros})

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

def deletecooviahorro(request, id):
    cooviahoroo = TasasCooviahorro.objects.get(id=id)
    cooviahoroo.delete()
    return redirect("cooviahorro")

class ApiCdat(viewsets.ModelViewSet):
    serializer_class =  CdatSerializer
    queryset = TasasCDAT.objects.all()
    

class ApiCooviahorro(viewsets.ModelViewSet):
    serializer_class =  CooviahorroSerializer
    queryset = TasasCooviahorro.objects.all()