from django import forms
from .models import *


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
