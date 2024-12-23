from django.shortcuts import render
from .models import Sucursal, Asesores

def sucursalList(request):
    sucursales = Sucursal.objects.all() 
    return render(request, 'sucursal.html', {'sucursales': sucursales})

def asesoresList(request):
    asesores = Asesores.objects.all()  
    return render(request, 'asesores.html', {'asesores': asesores})
