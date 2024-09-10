from rest_framework import serializers
from .models import *


class CdatSerializer(serializers.ModelSerializer):
    class Meta:
        model = TasasCDAT
        fields = '__all__'