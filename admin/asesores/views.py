from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import *
from .models import Sucursal, Asesores
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q

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
def asesorCreate(request):
    # Obtener parámetro de búsqueda
    search_query = request.GET.get('search', '').strip()
    update = False

    # Obtener lista de asesores con filtro aplicado
    asesores = Asesores.objects.all()
    if search_query:
        asesores = asesores.filter(
            Q(name__icontains=search_query) | Q(document__icontains=search_query)
        )

    # Configuración de paginación
    page = request.GET.get('page', 1)
    paginator = Paginator(asesores, 2)
    try:
        asesores = paginator.page(page)
    except Exception as e:
        messages.error(request, 'Error al paginar los asesores: {}'.format(e))
        asesores = paginator.page(1)

    # Procesar formulario de creación de asesor
    if request.method == 'POST':
        formNum = request.POST.get("form_id")
        if formNum == "form-created-asesor":
            form = AsesoresForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, '¡Asesor registrado con éxito!')
                return redirect('asesoresList')
        elif str(formNum).startswith("form-update-asesor"):
            asesor = Asesores.objects.get(id=formNum.split("-")[-1])
            form = AsesoresForm(request.POST, instance=asesor)
            if form.is_valid():
                form.save()
                messages.success(request, '¡Asesor actualizado con éxito!')
                return redirect('asesoresList') 
        else:
            currentId = formNum.split("-")[-1]
            update = True
            form = AsesoresForm(instance=Asesores.objects.get(id=currentId))
    else:
        form = AsesoresForm()

    return render(
        request, 
        'asesores.html', 
        {
            'form': form, 
            'update': update,
            'asesores': asesores, 
            'paginator': paginator, 
            'current_page': asesores,
            'search_query': search_query,
        }
    )


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
