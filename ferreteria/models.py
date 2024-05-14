from django.db import models
from django.contrib.auth.models import User

class Cliente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='cliente')
    # nro_cel = models.PositiveIntegerField()  # Elimina o comenta esta línea

class Bodeguero(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='bodeguero')
    # nro_cel_bod = models.PositiveIntegerField()  # Elimina o comenta esta línea

class Contador(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='contador')
    # nro_cel_cont = models.PositiveIntegerField()  # Elimina o comenta esta línea
