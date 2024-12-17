from django import forms
from .models import *

class SucursalForm(forms.ModelForm):
    class Meta:
        model = Sucursal
        fields = ["name"]
        labels = {
            "name": "Nombre Sucursal"
        }

class AsesoresForm(forms.ModelForm):
    class Meta:
        model = Asesores
        fields = ["name", "document", "sucursal"]
        labels = {
            "name": "Nombre Asesor",
            "document": "Numero de documento",
            "sucursal": "Sucursal"
        }