#encoding:utf-8
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Apunte (models.Model):
    nombre = models.CharField(max_length=128)
    tipo = models.IntegerField(default=0)
    fecha_creacion = models.CharField(max_length=128)
    hora_creacion = models.CharField(max_length=128)
    recurso = models.CharField(max_length=200)
    url = models.CharField(max_length=200)

    fecha_subida = models.DateField(auto_now_add=True)
    apute_id= models.AutoField(primary_key=True)
    codido_creador=models.CharField(max_length=20)

    def __unicode__(self):
        return unicode("{'nombre'"+ self.nombre+"}")

# class Notificacion(models.Model):
# 
