from django import forms
from .models import *

class SucursalForm(forms.ModelForm):
    class Meta():
        model = Sucursal
        fields = ['name']
        
class AsesoresForm(forms.ModelForm):
    class Meta():
        model = Asesores
        fields = ['name', 'document', 'sucursal']

