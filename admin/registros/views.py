from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializer import *

class RegistroCreditosView(viewsets.ModelViewSet):
    serializer_class = RegistrosSimulacionesCreditoSerializer
    queryset = RegistrosSimulacionesCreditos.objects.all()