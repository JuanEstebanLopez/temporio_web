"""temporio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from temporio_web import views;
from temporio_web.views import Home, InicioProfesor, TableroProfesor, vistaNotificaciones,vistaApuntes;

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', Home.as_view(), name='index'),
    url(r'^profesor/(?P<codigo>[-_\w]+)/$', InicioProfesor.as_view(), name='index'),
    url(r'^profesor/(?P<codigo>[-_\w]+)/tareas/$', TableroProfesor.as_view(), name='index'),
    # url(r'^crear_alarma/(?P<dia>[0-9]+)/(?P<mes>[0-9]+)/(?P<anio>[0-9]+)/(?P<hora>[-_\w]+)/(?P<minuto>[-_\w]+)/(?P<tipo>[0-9]+)/(?P<titulo>[-_\w]+)/(?P<descripcion>[-_\w]+)/(?P<materia>[-_\w]+)/$', views.crearNuevaNotificacion, name='crear_notificacion_sin_grupo'),
    url(r'^crear_alarma/(?P<dia>[0-9]+)/(?P<mes>[0-9]+)/(?P<anio>[0-9]+)/(?P<hora>[-_\w]+)/(?P<minuto>[-_\w]+)/(?P<tipo>[0-9]+)/(?P<titulo>[ -_\w]+)/(?P<descripcion>[ -_\w]+)/(?P<grupo>[-_\w]+)/$', views.crearNuevaNotificacionGrupo, name='crear_notificacion_con_grupo'),
    url(r'^notificaciones/estudiante/(?P<codigo>[-_\w]+)/$', vistaNotificaciones.as_view(), name='index'),
    url(r'^apuntes/estudiante/(?P<codigo>[-_\w]+)/$', vistaApuntes.as_view(), name='index'),
    # url(r'^j', views.post_list,name="in"),
]
