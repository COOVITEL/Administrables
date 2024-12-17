from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializer import *
from rest_framework.permissions import IsAuthenticated

class RegistroCreditosView(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    serializer_class = RegistrosSimulacionesCreditoSerializer
    queryset = RegistrosSimulacionesCreditos.objects.all()
    # http_method_names = ["post"]

class RegistroCdatView(viewsets.ModelViewSet):
    serializer_class = RegistrosSimulacionesCdatSerializer
    queryset = RegistroSimulacionesCdat.objects.all()
    http_method_names = ["post"]
