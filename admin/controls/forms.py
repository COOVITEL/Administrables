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

class NoSocialesForm(forms.ModelForm):
    """"""
    class Meta():
        model = NoSociales
        fields = ['name', 'usura', 'descuentos', 'techoEA', 'techoNMV', 'plazo']
        labels = {
            'name': 'Nombre',
            'usura': 'Tasa usura consumo',
            'descuento': 'Puntos de Descuentos al Asociado',
            'techoEA': 'Techo EA',
            'techoNMV': 'Techo NMV',
            'plazo': 'Plazo maximo de solicitud'
        }

class TypesAsociadoForm(forms.ModelForm):
    """"""
    class Meta():
        model = TypeAsociado
        fields = ['name']
        labels = {
            'name': 'Nombre del tipo de afiliación del asociado'
        }

class TasasNoSocialesForm(forms.ModelForm):
    """"""
    class Meta():
        model = TasasNoSociales
        fields = ['perfil', 'maxScore', 'minScore', 'fg', 'plazo', 'garantia', 'piso']
        labels = {
            'perfil': 'Tipo de perfil', 
            'maxScore': 'Score Maximo',
            'minScore': 'Score Minimo',
            'fg': 'F.G.',
            'plazo': 'Plazo Maximo',
            'garantia': 'Garantía',
            'piso': 'Piso'
        }

class FidelizacionForm(forms.ModelForm):
    """"""
    class Meta():
        model = Fidelizacion
        fields = ['name', 'porcentaje', 'tasa6', 'tasa12', 'tasa24', 'tasa36', 'tasa48', 'tasa60', 'tasa72', 'plazoMax', 'garantia']
        labels = {
            'name': 'Nombre',
            'porcentaje': 'Valor maximo de aportes a solicitar',
            'tasa6': 'Tasa a 6 cuotas',
            'tasa12': 'Tasa a 12 cuotas',
            'tasa24': 'Tasa a 24 cuotas',
            'tasa36': 'Tasa a 36 cuotas',
            'tasa48': 'Tasa a 48 cuotas',
            'tasa60': 'Tasa a 60 cuotas',
            'tasa72': 'Tasa a 72 cuotas',
            'plazoMax': 'Plazo maximo de cuotas',
            'garantia': 'Garantía'
        }


class SolcialesForm(forms.ModelForm):
    """"""
    class Meta():
        model = Sociales
        fields = ['name', 'tasa6', 'tasa12', 'tasa24', 'tasa36', 'tasa48', 'tasa60', 'tasa72', 'tasa84', 'plazoMax']
        labels = {
            'name': 'Nombre',
            'tasa6': 'Tasa a 6 cuotas',
            'tasa12': 'Tasa a 12 cuotas',
            'tasa24': 'Tasa a 24 cuotas',
            'tasa36': 'Tasa a 36 cuotas',
            'tasa48': 'Tasa a 48 cuotas',
            'tasa60': 'Tasa a 60 cuotas',
            'tasa72': 'Tasa a 72 cuotas',
            'tasa84': 'Tasa a 84 cuotas',
            'plazoMax': 'Plazo maximo de cuotas',
        }

class AsociadoTypeForm(forms.ModelForm):
    """"""
    class Meta():
        model = AsociadoType
        fields = ['name']
        labels = {
            'name': 'Nombre tipo de Asociado'
        }