from django.db import models

# Create your models here. As classe são as tabelas do banco

class Carros(models.Model):
    modelo = models.CharField(max_length=150)
    marca = models.CharField(max_length=100)
    ano = models.IntegerField()