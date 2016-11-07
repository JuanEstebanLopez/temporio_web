from django import template
from models import Apunte, Notificacion, Profesor, Estudiante, Materia, Grupo, CodigoGrupo
from django.contrib.contenttypes.models import ContentType
register = template.Library()

@register.filter(name='get_nombre_grupo')
def get_nombre_grupo(grupo):
    gru=Grupo.objects.get(codigo_grupo=grupo);
	return "G"+gru.numero_grupo+"_"+gru.nombre_materia;

@register.filter(name='get_hora_notificacion')
def get_hora_notificacion(noti):

	return "Hora";

@register.filter(name='get_fecha_notificacion')
def get_fecha_notificacion(noti):
 
	return "Fecha";
