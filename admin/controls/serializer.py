from rest_framework import serializers
from .models import *

class CdatSerializer(serializers.ModelSerializer):
    class Meta:
        model = TasasCDAT
        fields = '__all__'

class CooviahorroSerializer(serializers.ModelSerializer):
    class Meta:
        model = TasasCooviahorro
        fields = '__all__'

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