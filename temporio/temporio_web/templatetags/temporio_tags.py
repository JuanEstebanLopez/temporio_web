import datetime
from django.utils.timezone import utc
from django import template
from temporio_web.models import Apunte, Notificacion, Profesor, Estudiante, Materia, Grupo, CodigoGrupo
from django.contrib.contenttypes.models import ContentType
register = template.Library()

@register.filter(name='get_nombre_grupo')
def get_nombre_grupo(grupo):
    gru=Grupo.objects.get(codigo_grupo=grupo);
    cod="G"+str(gru.numero_grupo)+"_"+gru.nombre_materia;
    return cod;

@register.filter(name='get_hora_notificacion')
def get_hora_notificacion(noti):
    h=noti.tiempo_alarma.hour
    m=noti.tiempo_alarma.minute;
    hora="";
    if h<10:
        hora=hora+"0";
    hora=hora+str(h)+":";
    if m<10:
        hora=hora+"0";
    noti.tiempo_alarma.replace(tzinfo=utc)
    hora=hora+str(m);
    return hora;

@register.filter(name='get_fecha_notificacion')
def get_fecha_notificacion(noti):
    fecha=str(noti.tiempo_alarma.day)+"/"+str(noti.tiempo_alarma.month)+"/"+str(noti.tiempo_alarma.year);
    return fecha;
