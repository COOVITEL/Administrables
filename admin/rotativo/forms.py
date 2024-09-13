from django import forms
from .models import *


class AsociadoRotativoForm(forms.ModelForm):
    
    montoMax = forms.CharField(widget=forms.TextInput(attrs={'onInput': "handleChange('id_montoMax')"}), label="Monto Maximo a Solicitar")
    
    class Meta():
        model = AsociadoRotativo
        fields = ['name', 'montoMax', 'plazoMax', 'requisitos']
        labels = {
            'name': 'Nombre de tipo de Asociado',
            'plazoMax': 'Plazo maximo para el asociado',
            'requisitos': 'Requisitos (En caso de que aplique)'
        }

class EscenariosForm(forms.ModelForm):
    salarioMin = forms.CharField(widget=forms.TextInput(attrs={'onInput': "handleChange('id_salarioMin')"}), label="Salario Minimo")
    salarioMax = forms.CharField(widget=forms.TextInput(attrs={'onInput': "handleChange('id_salarioMax')"}), label="Salario Maximo", required=False)
    class Meta():
        model = Escenarios
        fields = ['name', 'salarioMin', 'salarioMax']
        labels = {
            'name': 'Nombre Escenario',
        }

class RotativoForm(forms.ModelForm):
    
    TYPES_RIESGOS = [
        ('Riesgo Bajo', 'Riesgo Bajo'),
        ('Riesgo Medio', 'Riesgo Medio'),
        ('Riesgo Alto', 'Riesgo Alto'),
    ]
    riesgo = forms.ChoiceField(
        choices=TYPES_RIESGOS,
        widget=forms.Select,
        label='Nivel de Riesgo',
        required=True)

    class Meta():
        model = Rotativo
        fields = ['typeAsociado', 'escenario', 'riesgo', 'scoreMin', 'scoreMax', 'EA', 'NMV', 'plazo']
        labels = {
            'escenario': 'Escenario',
            'typeAsociado': 'Perfil del asociado',
            'scoreMin': 'Score Minimo',
            'scoreMax': 'Score Maximo',
            'EA': 'EA (Tasa Anual)',
            'NMV': 'NMV (Tasa Mensual Nominal)',
            'plazo': 'Plazo'
            }