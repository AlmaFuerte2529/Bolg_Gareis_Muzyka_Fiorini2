from django.db import models

# Create your models here.

class Mensajes(models.Model):
    user=models.CharField(max_length=50)
    mensaje=models.TextField(max_length=250)
    autor=models.CharField(max_length=50)
    creado = models.DateTimeField(auto_now_add=True)
    leido=models.BooleanField(default=False)

    def __str__(self):
        return f"De: {self.autor}  -  Para: {self.user}"