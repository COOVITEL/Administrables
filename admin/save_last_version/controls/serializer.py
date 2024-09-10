from rest_framework import serializers
from .models import TasasCDAT, TasasCooviahorro

class CdatSerializer(serializers.ModelSerializer):
    class Meta:
        model = TasasCDAT
        fields = '__all__'

class CooviahorroSerializer(serializers.ModelSerializer):
    class Meta:
        model = TasasCooviahorro
        fields = '__all__'