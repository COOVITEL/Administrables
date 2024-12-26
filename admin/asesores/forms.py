from django import forms
from .models import *

class SucursalForm(forms.ModelForm):
    class Meta():
        model = Sucursal
        fields = ['name']
        labels = {
            'name': 'Nombre sucursal'
        }
        widget = {
            
        }
        
class AsesoresForm(forms.ModelForm):
    # sucursal = forms.ChoiceField(widget={forms.Select(attrs={'class': 'set-select'}, label="Sucursal")})
    class Meta():
        model = Asesores
        fields = ['name', 'document', 'sucursal']
        labels = {
            'name': 'Nombre Asesor',
            'document': 'Documento Asesor',
            'sucursal': 'Sucursal'
        }
        widgets = {
            'sucursal': forms.Select(attrs={
                'class': 'set-select'
            })
        }

