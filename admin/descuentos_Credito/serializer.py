from rest_framework import serializers
from .models import *


class AjustesScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = AjustesScore
        fields = '__all__'

class AjustesAportesSerializer(serializers.ModelSerializer):
    class Meta:
        model = AjustesAportes
        fields = '__all__'

class AjustesPlazoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AjustesPlazo
        fields = '__all__'

class AjustesCdatSerializer(serializers.ModelSerializer):
    class Meta:
        model = AjustesCDAT
        fields = '__all__'

class AjustesCooviahorroSerializer(serializers.ModelSerializer):
    class Meta:
        model = AjustesCooviahorro
        fields = '__all__'

class MaximoAjusteSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaximoAjuste
        fields = '__all__'