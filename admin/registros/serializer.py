from rest_framework import serializers
from .models import *

class RegistrosSimulacionesCreditoSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistrosSimulacionesCreditos
        fields = '__all__'