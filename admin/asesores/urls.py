# urls.py
from django.urls import path
from . import views
from . import list

urlpatterns = [
    path('sucursalCreate/', views.sucursalCreate, name='sucursalCreate'),
    path('asesorCreate/', views.asesorCreate, name='asesorCreate'),
    path('lista-sucursales/', list.sucursalList, name='sucursalList'),  
    path('lista-asesores/', list.asesoresList, name='asesoresList'),
    path('eliminar-asesor/<int:asesor_id>/', views.eliminar_asesor, name='eliminar_asesor'),
    path('eliminar-sucursal/<int:sucursal_id>/', views.eliminar_sucursal, name='eliminar_sucursal'),
]
