from django import forms
from .models import Usuarios

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuarios
        fields = ['nome', 'email', 'senha']
        widgets = {
            'email': forms.TextInput(attrs={'type': 'email'}),
            'senha': forms.PasswordInput()
        }

class LoginForm(forms.Form):
    email = forms.EmailField()
    senha = forms.CharField(widget=forms.PasswordInput())