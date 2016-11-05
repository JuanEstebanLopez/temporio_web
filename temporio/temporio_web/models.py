#encoding:utf-8
from __future__ import unicode_literals

import string
import random

from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class CodigoGrupo(models.Model):
    codigo= models.CharField(max_length=128); # codigo_materia-num_grupo
    def __unicode__(self):
        return unicode(self.codigo);

class Notificacion(models.Model):
    titulo= models.CharField(max_length=128);
    descripcion= models.CharField(max_length=128);
    fecha_alarma = models.DateField();
    tiempo_alarma = models.DateTimeField();
    tipo_repeticion=models.CharField(max_length=20);
    tipo_tarea = models.IntegerField(default=0);
    materia= models.CharField(max_length=128);
    # grupo_materia= models.CharField(max_length=128);
    grupos_materia_notificacion=models.ManyToManyField(CodigoGrupo,related_name='grupos_materia_notificacion',blank=True);
    # estado: 1-activo, 0-incompleta, 2-completa
    estado = models.IntegerField(default=1);
    str_fecha=models.CharField(max_length=128);
    def __unicode__(self):
        return unicode(self.str_fecha+"-"+self.tipo_repeticion+"-"+str(self.tipo_tarea)+"-"+self.materia+"-"+self.titulo+"-"+self.descripcion+"-"+str(self.estado));


class Apunte (models.Model):
    nombre = models.CharField(max_length=128);
    tipo = models.IntegerField(default=0);
    fecha_creacion = models.CharField(max_length=128);
    hora_creacion = models.CharField(max_length=128);
    recurso = models.CharField(max_length=200);
    url = models.CharField(max_length=200);
    fecha_subida = models.DateField(auto_now_add=True);
    # apute_id= models.AutoField(primary_key=True); -> pk
    codido_creador=models.CharField(max_length=20);
    def __unicode__(self):
        return unicode("{'nombre'"+ self.nombre+"}");


class Profesor(models.Model):
    user = models.OneToOneField(User);
    codigo = models.CharField(max_length=20,unique=True);
    nombre = models.CharField(max_length=50);
    grupos=models.ManyToManyField(CodigoGrupo,related_name='grupos_profesor',blank=True);
    def __unicode__(self):
        return unicode( self.codigo+"-"+self.nombre);

class  Estudiante(models.Model):
    user = models.OneToOneField(User);
    codigo = models.CharField(max_length=20,unique=True);
    nombre = models.CharField(max_length=50);
    materias = models.ManyToManyField(CodigoGrupo,related_name='materias_estudiante',blank=True); # id de grupo (horario)
    apuntes_compartidos = models.ManyToManyField(Apunte,related_name='compartidos',blank=True);
    apuntes_favoritos = models.ManyToManyField(Apunte,related_name='favoritos',blank=True);
    notificaciones_propias = models.ManyToManyField(Notificacion,related_name='notificaciones',blank=True); # id de grupo
    def __unicode__(self):
        return unicode( self.codigo+"-"+self.nombre);

class Horario (models.Model):
    salon = models.CharField(max_length=10);
    hora_inicio = models.CharField(max_length=10);
    hora_fin = models.CharField(max_length=10);
    dia = models.CharField(max_length=10);
    grupo = models.ForeignKey(CodigoGrupo,related_name='grupo_horario_materia',blank=True,null=True);
    def __unicode__(self):
        return unicode( self.dia+" "+self.hora_inicio+"-"+self.hora_fin+" "+self.salon);

class Grupo(models.Model):
    codigo_grupo = models.OneToOneField(CodigoGrupo,blank=True);# codigo_materia-num_grupo
    nombre_materia = models.CharField(max_length=128);
    numero_grupo = models.IntegerField(default=0);
    horario = models.ManyToManyField(Horario,related_name='horarios_del_grupo');
    profesor= models.ForeignKey(Profesor);
    estudiantes = models.ManyToManyField(Estudiante,blank=True);
    def __unicode__(self):
        return unicode( self.codigo_grupo);

class Materia(models.Model):
    nombre = models.CharField(max_length=128);
    codigo = models.CharField(max_length=20);
    grupos= models.ManyToManyField(Grupo,related_name='grupos_materia',blank=True);
    def __unicode__(self):
        return unicode( self.codigo+"-"+self.nombre);
