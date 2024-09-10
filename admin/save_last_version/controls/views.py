import requests
import pandas as pd
import os
from datetime import datetime
from django.shortcuts import render, redirect, HttpResponse
from .models import TasasCDAT, TasasCooviahorro
from .forms import CreateUserForm, LoginForm, Scores
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializer import CdatSerializer, CooviahorroSerializer
from django.contrib import messages

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
@login_required(login_url="login")
def createCdat(request):
    if request.method == 'POST':
        person = request.POST['person']
        type = request.POST['type']
        since = request.POST['since']
        until = request.POST['until']
        amountsince = request.POST['amountsince']
        amountuntil = request.POST['amountuntil']
        tasa = request.POST['tasa']

        create = TasasCDAT(person=person,  type=type, since=since, until=until, amountsince=amountsince, amountuntil=amountuntil, tasa=tasa)
        create.save()
        return redirect('cdats')
    return render(request, 'createcdat.html')
# Update cdat
@login_required(login_url="login")
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

@login_required(login_url="login")
def deletecdat(request, id):
    cdat = TasasCDAT.objects.get(id=id)
    cdat.delete()
    return redirect('cdats')
        

# Return all Cooviahorros controls
@login_required(login_url="login")
def Cooviahorro(request):
    ahorros = TasasCooviahorro.objects.all()
    
    return render(request, 'cooviahorro.html', {'ahorros': ahorros})

@login_required(login_url="login")
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
@login_required(login_url="login")
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


@login_required(login_url="login")
def deletecooviahorro(request, id):
    cooviahoroo = TasasCooviahorro.objects.get(id=id)
    cooviahoroo.delete()
    return redirect("cooviahorro")


@login_required(login_url="login")
def downloadDates(request):
    response = requests.get("http://192.168.1.16:8005/turns/api/v1/turns/")
    dates = response.json()
    
    df = pd.DataFrame(dates)
    df.to_excel('controls/static/datos.xlsx', index=False)

    file_path = os.path.join('controls/static/', 'datos.xlsx')
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    else:
        return redirect("admin")


@login_required(login_url="login")
def DatesDigiTurn(request):
    response = requests.get("http://192.168.1.16:8005/turns/api/v1/turns/")
    list_dates = response.json()

    list_dates = [item for item in list_dates if item.get("score_time") == "empty"]

    city = request.GET.get("city")
    date = request.GET.get("fecha")
    now = datetime.now()
    day = now.day
    
    if city is not None:
        list_dates = [item for item in list_dates if item.get("city") == city]
    if date == "1":
        list_dates = [item for item in list_dates if str(item.get("date")[-2:]) == str(day)]
    if date == "3":
        list_dates = [item for item in list_dates if int(item.get("date")[-2:]) >= int(day - 3)]
    if date == "7":
        list_dates = [item for item in list_dates if int(item.get("date")[-2:]) >= int(day - 7)]
    
    context = {
        "dates": list_dates,
        "date": day
    }        

    return render(request, "dates.html", context=context)

@login_required(login_url="login")
def updateTurn(request, id):
    """"""
    response = requests.get(f"http://192.168.1.16:8005/turns/api/v1/turns/{id}/")
    turn = response.json()
    copy = turn
    form = Scores()
    if request.method == "POST":
        form = Scores(request.POST)
        if form.is_valid():
            copy["score_time"] = request.POST.get('time')
            copy["score_service"] = request.POST.get('attention')
            copy["score_att"] = request.POST.get('service')
            copy["score_recommen"] = request.POST.get('recomment')
            copy["state"] = "by_call"
            requests.put(f"http://192.168.1.16:8005/turns/api/v1/turns/{id}/", data=copy)
            messages.success(request, "Las calificaciones se actualizaron de forma correcta!")
            return redirect("dates")
            
    
    return render(request, "updatescore.html", {"turn": turn, "scores": form})

class ApiCdat(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class =  CdatSerializer
    queryset = TasasCDAT.objects.all()
    

class ApiCooviahorro(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class =  CooviahorroSerializer
    queryset = TasasCooviahorro.objects.all()