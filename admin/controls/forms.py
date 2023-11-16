from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from django.forms.widgets import PasswordInput, TextInput


# - Create/Register User

class CreateUserForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label="Usuario")
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}), label="Email")
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), label="Contraseña")
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), label="Confirme Contraseña")
# - Authetication User

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput(attrs={'class': 'user-input'}), label="Usuario")
    password = forms.CharField(widget=PasswordInput(), label="Contraseña")


class Scores(forms.Form):
    CHOICES_TIME = [
        ("", "-- Seleccione --"),
        ('Muy rápido', 'Muy rápido'),
        ('Rápido', 'Rápido'),
        ('Normal', 'Normal'),
        ('Lento', 'Lento'),
        ('Muy Lento', 'Muy Lento'),
    ]

    CHOICES_ATT = [
        ('', '-- Selecciona --'),
        ('Excelente', 'Excelente'),
        ('Bueno', 'Bueno'),
        ('Normal', 'Normal'),
        ('Regular', 'Regular'),
        ('Malo', 'Malo'),
    ]

    CHOICES_SERVICE = [
        ('', '-- Selecciona --'),
        ('Si', 'Si'),
        ('No', 'No'),
    ]

    CHOICES_REC = [
        ('', '-- Selecciona --'),
        ('Si', 'Si'),
        ('Tal vez', 'Tal vez'),
        ('No', 'No'),
    ]

    time = forms.ChoiceField(choices=CHOICES_TIME, label="Tiempo espera?")
    attention = forms.ChoiceField(choices=CHOICES_ATT, label="Servicio brindado?")
    service = forms.ChoiceField(choices=CHOICES_SERVICE, label="Solicitud atendida?")
    recomment = forms.ChoiceField(choices=CHOICES_REC, label="Recomendaria Coovitel?")