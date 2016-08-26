from django.db import models
from django.utils import timezone
from website import *

# Create your models here.

class com_aerea(models.Model):
    id = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=30)

    def __str__(self):
        return self.id

class cidade(models.Model):
    id = models.CharField(max_length=3, primary_key=True)
    nome = models.CharField(max_length=30)

    def __str__(self):
        return self.id

class voo(models.Model):
    id = models.IntegerField(primary_key=True)
    id_com_aerea = models.ForeignKey('website.com_area')
    data_decolagem = models.DateTimeField()
    data_pouso = models.DateTimeField()
    id_origem = models.ForeignKey('website.cidade')
    id_destino = models.ForeignKey('website.cidade')
    preco = models.FloatField()
    assentos_totais = models.IntegerField()

    def __str__(self):
        return self.id
