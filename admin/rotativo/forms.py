from django import forms
from .models import *


class EscenariosForm(forms.ModelForm):
    salarioMin = forms.CharField(widget=forms.TextInput(attrs={'onInput': "handleChange('id_salarioMin')"}), label="Salario Minimo")
    salarioMax = forms.CharField(widget=forms.TextInput(attrs={'onInput': "handleChange('id_salarioMax')"}), label="Salario Maximo")
    class Meta():
        model = Escenarios
        fields = ['name', 'salarioMin', 'salarioMax']
        labels = {
            'name': 'Nombre Escenario',
        }

class RotativoForm(forms.ModelForm):
    TYPES_ASOCIADOS = [
        ('Pensionado', 'Pensionado'),
        ('Convenio', 'Convenio')
    ]
    typeAsociado = forms.ChoiceField(
        choices=TYPES_ASOCIADOS,
        widget=forms.Select,
        label='Tipo de Asociado',
        required=True
    )
    class Meta():
        model = Rotativo
        fields = ['escenario', 'riesgo', 'typeAsociado', 'scoreMin', 'scoreMax', 'EA', 'NMV', 'plazo']
        labels = {
            'escenario': 'Escenario',
            'riesgo': 'Nivel de Riesgo',
            'scoreMin': 'Score Minimo',
            'scoreMax': 'Score Maximo',
            'EA': 'EA (Tasa Anual)',
            'NMV': 'NMV (Tasa Mensual Nominal)',
            'plazo': 'Plazo'
            }