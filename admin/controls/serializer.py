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

class TypeAsociadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeAsociado
        fields = '__all__'