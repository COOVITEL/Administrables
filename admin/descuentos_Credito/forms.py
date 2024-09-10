from django import forms
from .models import *

class AjustesScoreForm(forms.ModelForm):
    """"""
    class Meta():
        model = AjustesScore
        fields = ['asociado', 'scoreMin', 'scoreMax', 'ajuste']
        labels = {
            'asociado': 'Ajuste dirigido a',
            'scoreMin': 'Score minimo a aplicar',
            'scoreMax': 'Score maximo a aplicar',
            'ajuste': 'Ajuste de tasa'
        }

class AjustesAportesForm(forms.ModelForm):
    """"""
    aporteMin = forms.CharField(widget=forms.TextInput(attrs={'oninput': "handleChange('id_aporteMin')"}),
                            label="Monto minimo de aportes")
    aporteMax = forms.CharField(widget=forms.TextInput(attrs={'oninput': "handleChange('id_aporteMax')"}),
                            label="Monto maximo de aportes")
    class Meta():
        model = AjustesAportes
        fields = ['asociado', 'aporteMin', 'aporteMax', 'ajuste']
        labels = {
            'asociado': 'Ajuste dirigido a',
            'ajuste': 'Ajuste de tasa'
        }

class AjustesPlazoForm(forms.ModelForm):
    """"""
    class Meta():
        model = AjustesPlazo
        fields = ['asociado', 'plazoMin', 'plazoMax', 'ajuste']
        labels = {
            'asociado': 'Ajuste dirigido a',
            'plazoMin': 'Plazo minimo a aplicar',
            'plazoMax': 'Plazo maximo a aplicar',
            'ajuste': 'Ajuste de tasa'
        }

class AjustesCDATForm(forms.ModelForm):
    """"""
    montoMin = forms.CharField(widget=forms.TextInput(attrs={'oninput': "handleChange('id_montoMin')"}),
                            label="Monto Minimo")
    montoMax = forms.CharField(widget=forms.TextInput(attrs={'oninput': "handleChange('id_montoMax')"}),
                            label="Monto Maximo")
    class Meta():
        model = AjustesCDAT
        fields = ['montoMin', 'montoMax', 'ajuste']
        labels = {
            'ajuste': 'Ajuste de tasa'
        }

class AjustesCooviahorroForm(forms.ModelForm):
    """"""
    montoMin = forms.CharField(widget=forms.TextInput(attrs={'oninput': "handleChange('id_montoMin')"}),
                            label="Monto Minimo")
    montoMax = forms.CharField(widget=forms.TextInput(attrs={'oninput': "handleChange('id_montoMax')"}),
                            label="Monto Maximo")
    class Meta():
        model = AjustesCooviahorro
        fields = ['montoMin', 'montoMax', 'ajuste']
        labels = {
            'ajuste': 'Ajuste de tasa'
        }

class MaximoAjustesForm(forms.ModelForm):
    TYPES = [
    ('Score', 'Score'),
    ('Aportes', 'Aportes'),
    ('Plazo', 'Plazo'),
    ('Cdat', 'Cdat'),
    ('Cooviahorro', 'Cooviahorro'),
]
    """"""
    name = forms.ChoiceField(
        required=True,
        widget=forms.RadioSelect,
        choices=TYPES,
        label="Tipo de descuento"
    )
    class Meta:
        model = MaximoAjuste
        fields = ['name', 'value']
        labels = {
            'value': 'Porcentaje de descuento'
        }