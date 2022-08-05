from django.db import models
from django.contrib.auth.models import User




class Entrada(models.Model):
    titulo = models.CharField(max_length=80)
    contenido = models.TextField(max_length=400)
    fecha_ingreso = models.DateField(auto_now_add=True)
    imagen = models.ImageField(upload_to='entrada', null=True, blank=True)
    autor = models.CharField(max_length=50)

    def __str__(self):
        return self.titulo

class Avatar(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    imagen= models.ImageField(upload_to='avatares', null=True, blank=True)

class Comentario(models.Model):
    nombre = models.CharField(max_length=50)
    comentario = models.TextField(max_length=400)