from django.db import models

# Create your models here.

class Usuari(models.Model):
    nom = models.CharField(max_length=50)
    cognom = models.CharField(max_length=50)
    correu = models.CharField(max_length=50)
    rol = models.CharField(max_length=50)
    moduils = models.CharField(max_length=50)