from rest_framework import serializers
from .models import *


class AsociadosRotativoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AsociadoRotativo
        fields = '__all__'


class EscenariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Escenarios
        fields = '__all__'


class RotativosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rotativo
        fields = '__all__'