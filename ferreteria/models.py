from django.db import models

# Create your models here.

class Cliente(models.Model):
    codigo = models.CharField(max_length=3, primary_key=true)
    nombre = models.CharField(max_length=50)
    correo = models.CharField(max_length=80)
