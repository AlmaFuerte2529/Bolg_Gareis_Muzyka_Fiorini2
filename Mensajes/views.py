from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from Mensajes.models import Mensajes
from Mensajes.forms import FormMensajes

# Create your views here.

nombre_temp =""

def mensajes(request):
    mensajes = Mensajes.objects.filter(user=request.user)
    return render(request, "mensajes.html", {'mensajes':mensajes})

def mensaje(request, msg_id):
    mensaje = Mensajes.objects.get(id=msg_id)
    return render(request, "mensaje.html", {'mensaje':mensaje})

def enviar(request, nombre):
    global nombre_temp
    nombre_temp = nombre
    form= FormMensajes(initial={"user":nombre, "autor":request.user})
    return render(request, "formMensaje.html", {"formulario":form})

def formMensajes(request):
    if (request.method=="POST"):
        form= FormMensajes(request.POST)
        if form.is_valid():
            info= form.cleaned_data
            autor = request.user
            nombre = nombre_temp
            msj= info["mensaje"]
            mensaje = Mensajes(user=nombre, autor=autor, mensaje=msj)
            mensaje.save()
            return redirect('mensajes')
    else:
        form= FormMensajes(initial={"user":nombre, "autor":request.user})
    
    return render(request, "formMensaje.html", {"formulario":form})

def listaUsuarios(request):
    usuarios = User.objects.all()
    return render(request, "usuarios.html", {"usuarios":usuarios})


def borrar(request, msg_id):
    mensaje = Mensajes.objects.get(id=msg_id)
    mensaje.delete()
    return redirect('mensajes')