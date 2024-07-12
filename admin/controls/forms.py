from django import forms
from .models import *

TYPES_PERSON = [
    ('NATURAL', 'NATURAL'),
    ('JURIDICA', 'JURIDICA'),
]

TYPE_CDAT = [
    ('ACTUAL', 'ACTUAL'),
    ('CAMPAÑA', 'CAMPAÑA')
]

class TasasCDATForm(forms.ModelForm):
    """"""
    person = forms.ChoiceField(
        required=True,
        widget=forms.RadioSelect,
        choices=TYPES_PERSON,
        label="Seleccione el tipo de persona a la cual aplicara el CDAT"
    )
    
    type = forms.ChoiceField(
        required=True,
        widget=forms.RadioSelect,
        choices=TYPE_CDAT,
        label="Seleccione el tipo de CDAT"
    )
    
    since = forms.CharField(widget=forms.TextInput(attrs={'oninput': "handleChange('id_since')"}),
                            label="Monto minimo a aplicar")
    until = forms.CharField(widget=forms.TextInput(attrs={'oninput': "handleChange('id_until')"}),
                            label="Monto maximo a aplicar")
    
    class Meta():
        model = TasasCDAT
        fields = ['person', 'type', 'since', 'until', 'amountsince', 'amountuntil', 'tasa']
        labels = {
            'amountsince': 'Numero minimo de dias',
            'amountuntil': 'Numero maximo de dias',
            'tasa': 'Tasa a aplicar'
        }

class TasasCooviahorroForm(forms.ModelForm):
    """"""
    amountMin = forms.CharField(widget=forms.TextInput(attrs={'oninput': "handleChange('id_amountMin')"}),
                                label="Monto Minimo")

    class Meta():
        model = TasasCooviahorro
        fields = ['type', 'amountMin', 'termMin', 'tasa']
        labels = {
            'type': 'Nombre del Cooviahorro',
            'termMin': 'Plazo minimo en meses',
            'tasa': 'Tasa',
        }