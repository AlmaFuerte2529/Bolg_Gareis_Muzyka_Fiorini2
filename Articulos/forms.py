from django import forms
from .models import Entrada
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User




class EntradaForm(forms.ModelForm):
    titulo = forms.CharField(max_length=80, widget=forms.TextInput)
    contenido = forms.CharField(widget=forms.Textarea)
    imagen = forms.ImageField()
    autor = forms.CharField(max_length=50, disabled = True, widget=forms.TextInput)


    class Meta:
        model= Entrada
        fields= ["titulo", "contenido", "imagen", "autor"]
    

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label="Usuario")
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}

class AvatarForm(forms.Form):
    imagen= forms.ImageField(label="Imagen")


class UserEditForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput)

    first_name= forms.CharField(max_length=50)
    last_name= forms.CharField(max_length=50)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name']
        help_texts = {k:"" for k in fields}


class ComentarioForm(forms.Form):
    nombre = forms.CharField(label='Nombre :', max_length=50)
    comentario = forms.CharField(widget=forms.Textarea)

