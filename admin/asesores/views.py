from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import *
from .models import Sucursal, Asesores
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404

@login_required
def sucursalCreate(request):
    form = SucursalForm()
    sucursales = Sucursal.objects.all()
    
    if request.method == 'POST':
        form = SucursalForm(request.POST)
        if form.is_valid():
            form.save() 
            messages.success(request, '¡Sucursal registrada con éxito!')  
            return redirect('sucursalList')

    return render(request, 'sucursal.html', {'form': form, 'sucursales': sucursales})

@login_required
def asesorCreate(request, ):
    if request.method == 'POST':
        form = AsesoresForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Asesor registrado con éxito!')
            return redirect('asesoresList')
    else:
        form = AsesoresForm()

    asesores = Asesores.objects.all()  
    return render(request, 'asesores.html', {'form': form, 'asesores': asesores})

@csrf_exempt
@login_required
def eliminar_asesor(request, asesor_id):
    if request.method == 'DELETE':
        asesor = get_object_or_404(Asesores, id=asesor_id)
        asesor.delete()
        return JsonResponse({'message': 'Asesor eliminado correctamente.'}, status=200)
    return JsonResponse({'error': 'Método no permitido.'}, status=405)

@login_required
@csrf_exempt
def eliminar_sucursal(request, sucursal_id):
    if request.method == 'DELETE':
        sucursal = get_object_or_404(Sucursal, id=sucursal_id)
        sucursal.delete()
        return JsonResponse({'message': 'Sucursal eliminada correctamente.'}, status=200)
    return JsonResponse({'error': 'Método no permitido.'}, status=405)
