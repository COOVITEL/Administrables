from rest_framework import serializers
from .models import *

class NoSocialesSerializer(serializers.ModelSerializer):
    class Meta:
        model = NoSociales
        fields = '__all__'

class SocialesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sociales
        fields = '__all__'


class FidelizacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fidelizacion
        fields = '__all__'

class TasasSerializer(serializers.ModelSerializer):
    class Meta:
        model = TasasNoSociales
        fields = '__all__'

class TypeAsociadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeAsociado
        fields = '__all__'