# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('lista-sucursales/', views.sucursalCreate, name='sucursalList'),
    path('lista-asesores/', views.asesorCreate, name='asesoresList'),
    path('eliminar-asesor/<int:asesor_id>/', views.eliminar_asesor, name='eliminar_asesor'),
    path('eliminar-sucursal/<int:sucursal_id>/', views.eliminar_sucursal, name='eliminar_sucursal'),
    path('obtener-asesor/<int:asesor_id>/', views.obtener_asesor, name='obtener_asesor'),
    path('editar-asesor/<int:asesor_id>/', views.editar_asesor, name='editar_asesor'),
    
]
