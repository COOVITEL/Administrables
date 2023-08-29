from django.shortcuts import render
from django.http import HttpResponse
from .models import TasasCDAT, TasasCooviahorro

def Index(request):
    return render(request, 'authentication/index.html')

def Register(request):
    return render(request, 'authentication/register.html')


def login(request):
    return render(request, 'authentication/login.html')

def Cdat(request):
    cdats = TasasCDAT.objects.all()
    return render(request, 'cdat.html', {'cdats': cdats})

def Cooviahorro(request):
    ahorros = TasasCooviahorro.objects.all()
    return render(request, 'ahorros.html', {'ahorros': ahorros})

