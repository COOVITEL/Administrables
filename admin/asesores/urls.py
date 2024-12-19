# urls.py
from django.urls import path
from . import views
from . import list

urlpatterns = [
    path('sucursalCreate/', views.sucursalCreate, name='sucursalCreate'),
    path('asesorCreate/', views.asesorCreate, name='asesorCreate'),
    path('sucursalList/', list.sucursalList, name='sucursalList'),  
    path('asesoresList/', list.asesoresList, name='asesoresList'),
]
