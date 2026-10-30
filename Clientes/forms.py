from django import forms
from .models import InscripcionTaller

class InscripcionTallerForm(forms.ModelForm):
    class Meta:
        model = InscripcionTaller
        fields = ['nombre_completo', 'email', 'taller', 'alimento_donado']
        widgets = {
            'nombre_completo': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Ingrese su nombre completo'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control', 
                'placeholder': 'ejemplo@correo.com'
            }),
            'taller': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Nombre del taller al que desea asistir'
            }),
            'alimento_donado': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Ej: 1 kg de fideos, arroz, etc.'
            }),
        }