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
import logging
import json

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

    # Obtener lista de asesores con filtro aplicado
    asesores = Asesores.objects.all()
    if search_query:
        asesores = asesores.filter(
            Q(name__icontains=search_query) | Q(document__icontains=search_query)
        )

    # Configuración de paginación
    page = request.GET.get('page', 1)
    paginator = Paginator(asesores, 5)
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
        elif formNum == "form-update-asesor":
            print("Se esta actualizando")
            id = 2
            form = AsesoresForm(instance=Asesores.objects.get(id=id))
            return render(
                request, 
                'asesores.html', 
                {
                    'form': form,
                    'asesores': asesores, 
                    'paginator': paginator, 
                    'current_page': asesores,
                    'search_query': search_query,
                }
            )
        else:
            print("Se abrio el formulario para actualizar")
            id = 2
            form = AsesoresForm(instance=Asesores.objects.get(id=id))
            return render(
                request, 
                'asesores.html', 
                {
                    'form': form,
                    'update': True,
                    'asesores': asesores, 
                    'paginator': paginator, 
                    'current_page': asesores,
                    'search_query': search_query,
                }
            )
    else:
        form = AsesoresForm()

    return render(
        request, 
        'asesores.html', 
        {
            'form': form, 
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

logger = logging.getLogger(__name__)
@csrf_exempt
@login_required
def obtener_asesor(request, asesor_id):
    try:
        if request.method == 'GET':
            logger.info(f"Solicitud para obtener asesor con ID: {asesor_id}")
            asesor = get_object_or_404(Asesores, id=asesor_id)
            logger.info(f"Asesor encontrado: {asesor}")
            
            if request.method == "POST":
                pass
            
            return JsonResponse({
                'name': asesor.name,
                'document': asesor.document,
                'sucursal': str(asesor.sucursal),  
            }, status=200)
        return JsonResponse({'error': 'Método no permitido.'}, status=405)
    except Exception as e:
        logger.error(f"Error al obtener asesor: {e}")
        return JsonResponse({'error': 'Error interno del servidor.'}, status=500)
    
@csrf_exempt
@login_required
def editar_asesor(request, asesor_id):
    if request.method == 'PUT':
        asesor = get_object_or_404(Asesores, id=asesor_id)
        try:
            data = json.loads(request.body)  # Parsear el cuerpo de la solicitud JSON
            for field, value in data.items():
                if field == 'sucursal' and value:  # Manejo de campo relacional
                    asesor.sucursal = get_object_or_404(Sucursal, id=value)
                elif hasattr(asesor, field):  # Verificar si el campo existe en el modelo
                    setattr(asesor, field, value)
            asesor.save()
            return JsonResponse({'message': 'Asesor se ha editado correctamente.'}, status=200)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Datos JSON inválidos.'}, status=400)
        except Exception as e:
            return JsonResponse({'error': f'Error al editar el asesor: {str(e)}'}, status=500)
    return JsonResponse({'error': 'Método no permitido.'}, status=405)
