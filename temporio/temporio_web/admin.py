from django.contrib import admin
from models import Apunte, Notificacion, Profesor,Estudiante,Horario,Grupo,Materia
# Register your models here.

admin.site.register(Notificacion);
admin.site.register(Apunte);
admin.site.register(Profesor);
admin.site.register(Estudiante);
admin.site.register(Horario);
admin.site.register(Grupo);
admin.site.register(Materia);
