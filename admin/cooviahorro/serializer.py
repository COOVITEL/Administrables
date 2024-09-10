from rest_framework import serializers
from .models import *

class CooviahorroSerializer(serializers.ModelSerializer):
    class Meta:
        model = TasasCooviahorro
        fields = '__all__'