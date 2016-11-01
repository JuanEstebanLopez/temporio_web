#encoding:utf-8
from __future__ import unicode_literals

import string
import random

from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Notificacion(models.Model):
    titulo= models.CharField(max_length=128)
    descripcion= models.CharField(max_length=128)
    fecha_alarma = models.DateField();
    tiempo_alarma = models.DateTimeField();

class Apunte (models.Model):
    nombre = models.CharField(max_length=128);
    tipo = models.IntegerField(default=0);
    fecha_creacion = models.CharField(max_length=128);
    hora_creacion = models.CharField(max_length=128);
    recurso = models.CharField(max_length=200);
    url = models.CharField(max_length=200);
    fecha_subida = models.DateField(auto_now_add=True);
    apute_id= models.AutoField(primary_key=True);
    codido_creador=models.CharField(max_length=20);
    def __unicode__(self):
        return unicode("{'nombre'"+ self.nombre+"}");


class Profesor(models.Model):
    user = models.OneToOneField(User);
    codigo = models.CharField(max_length=20,unique=True);
    nombre = models.CharField(max_length=50);
    grupos=models.ManyToManyField("self");



class Horario (models.Model):
    salon = models.CharField(max_length=10);
    hora_inicio = models.CharField(max_length=10);
    hora_fin = models.CharField(max_length=10);
    dia = models.CharField(max_length=10);
    def __unicode__(self):
        return unicode( self.dia+" "+self.hora_inicio+"-"+self.hora_fin+" "+self.salon);


class materia(models.Model):
    nombre = models.CharField(max_length=128);
    codigo = models.CharField(max_length=20);
