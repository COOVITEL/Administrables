from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import SucursalForm, AsesoresForm
from .models import Sucursal, Asesores

def sucursalCreate(request):
    if request.method == 'POST':
        form = SucursalForm(request.POST)
        if form.is_valid():
            form.save() 
            messages.success(request, '¡Sucursal registrada con éxito!')  
            return redirect('sucursalCreate')
    else:
        form = SucursalForm()

    sucursales = Sucursal.objects.all()  # Obtener todas las sucursales
    return render(request, 'sucursal.html', {'form': form, 'sucursales': sucursales})


def asesorCreate(request, ):
    if request.method == 'POST':
        form = AsesoresForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Asesor registrado con éxito!')
            return redirect('asesorCreate')
    else:
        form = AsesoresForm()

    asesores = Asesores.objects.all()  # Obtener todos los asesores
    return render(request, 'asesores.html', {'form': form, 'asesores': asesores})
