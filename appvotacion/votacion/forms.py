from .models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class DateInput(forms.DateInput):
    input_type = 'datetime-local'

class votacionForm(forms.ModelForm):
    class Meta:
        model = votacion
        fields = ('nombre','descripcion','fecha_inicio','fecha_fin')
        widgets = {
            'fecha_inicio': DateInput(attrs={'class': 'form-control'}),
            'fecha_fin': DateInput(attrs={'class': 'form-control'}),
        }

class votanteForm(forms.ModelForm):
    class Meta:
        model = votante
        fields = ('ide','nombre','apellido')

class candidatoForm(forms.ModelForm):
    class Meta:
        model = candidato
        fields = ('votante','tarjeton','imagen','descripcion')

class votosForm(forms.ModelForm):
    class Meta:
        model = votos
        fields = ('votacion','candidato','votante')

class eliminarForm(forms.Form):
    eliminar = forms.BooleanField(required=False)

class RegisterUserForm(UserCreationForm):
    class Meta:
        model = User
        fields =  ['username', 'email', 'password1', 'password2']
        
    def clean_email(self):
        correo = self.cleaned_data.get("email")
        email_already_registered = User.objects.filter(email = correo).exists()
        user_is_active = User.objects.filter(email = correo, is_active = 1)
        if email_already_registered and user_is_active:
            raise forms.ValidationError("Email already registered.")
        elif email_already_registered:
            User.objects.filter(email = correo).delete()
        return correo

class validarVotanteForm(forms.Form):
    nombre = forms.CharField(required=True,label="Primer Nombre")
    ide = forms.IntegerField(required=True,label="Número de Identificación")