from django import forms
from .models import *

class TypeAsociadoForm(forms.ModelForm):
    class Meta():
        model = TypeAsociado
        fields = ['name']
        labels = {
            'name': 'Nombre Tipo Asociado'
        }

class TypesRiesgosForm(forms.ModelForm):
    class Meta():
        model = TypesRiesgos
        fields = ['name']
        labels = {
            'name': 'Nombre Tipo Asociado'
        }

class EscenariosForm(forms.ModelForm):
    class Meta():
        model = Esecenarios
        fields = ['name', 'salarioMin', 'salarioMax']
        labels = {
            'name': 'Nombre Escenario',
            'salarioMin': 'Salario Minimo',
            'salarioMax': 'Salario Maximo'
        }