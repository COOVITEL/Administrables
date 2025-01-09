"""This module contains the views for the rest api."""
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render
from rest_framework import viewsets
from .serializer import (
    # RegistrosSimulacionesCooviahorroSerializer,
    RegistrosSimulacionesCreditoSerializer,
    # RegistrosSimulacionesCdatSerializer,
    # RegistrosSimulacionesRotativoSerializer)
)
from .models import (
    RegistroSimulacionCooviahorro,
    RegistroSimulacionRotativo,
    RegistrosSimulacionesCreditos,
    RegistroSimulacionesCdat
)

class RegistroCreditosView(viewsets.ModelViewSet):
    """
        This class defines the create behavior of our rest api.
    """
    permission_classes = [IsAuthenticated]
    serializer_class = RegistrosSimulacionesCreditoSerializer
    queryset = RegistrosSimulacionesCreditos.objects.all()
    http_method_names = ["post"]


# class RegistroCdatView(viewsets.ModelViewSet):
#     serializer_class = RegistrosSimulacionesCdatSerializer
#     queryset = RegistroSimulacionesCdat.objects.all()
#     http_method_names = ["post"]


# class RegistroRotativoView(viewsets.ModelViewSet):
#     permission_classes = [IsAuthenticated]
#     serializer_class = RegistrosSimulacionesRotativoSerializer
#     queryset = RegistroSimulacionRotativo.objects.all()
#     http_method_names = ["post"]


# class RegistroCooviahorroView(viewsets.ModelViewSet):
#     permission_classes = [IsAuthenticated]
#     serializer_class = RegistrosSimulacionesCooviahorroSerializer
#     queryset = RegistroSimulacionCooviahorro.objects.all()
#     http_method_names = ["post"]
