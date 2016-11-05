
# -*- coding: utf-8 -*-
from django.shortcuts import render
# import datetime
# import string
# import random
# import base64
# import hashlib
# import hmac
# import json as simplejson
# import time

from django.views.generic import View, FormView, UpdateView, CreateView, DetailView, ListView, TemplateView
# from django.contrib.auth import authenticate, login, logout
# from django.http import HttpResponseRedirect, HttpResponse
# from django.contrib.auth.decorators import login_required
# from django.core.urlresolvers import reverse
# from django.contrib import auth
# from django.contrib.auth.forms import AuthenticationForm
# from django.contrib.auth import REDIRECT_FIELD_NAME, login as auth_login, logout as auth_logout
# from django.utils.decorators import method_decorator
# from django.views.decorators.debug import sensitive_post_parameters
# from django.views.decorators.csrf import csrf_protect
# from django.utils.http import is_safe_url
# from django.views.decorators.cache import never_cache
#
# from django.dispatch import receiver
# from django.shortcuts import redirect
# from django.http import Http404
#
# from django.template import defaultfilters
# from django.template.defaultfilters import slugify

from models import Apunte, Notificacion, Profesor, Estudiante, Materia

"""
Método usado para pedir las notificaciones de un estudiante que han sido cradas por sus profesores.
"""
def getNotificacionesEstudiantes(estudiante):
    notis=set([]);
    grupos_estudiantes=estudiante.materias.all();
    todas_notis=Notificacion.objects.all();
    for n in todas_notis:
        for g in grupos_estudiantes:
            if g in n.grupos_materia_notificacion.all():
                notis.add(n);
    return notis;

"""
Método usado para pedir las notificaciones que un profesores ha creado para sus grupos.
"""
def getNotificacionesEstudiantes(profesor):
    notis=set([]);
    grupos_profesor=profesor.grupos.all();
    todas_notis=Notificacion.objects.all();
    for n in todas_notis:
        for g in grupos_profesor:
            if g in n.grupos_materia_notificacion.all():
                notis.add(n);
    return notis;

def getMateriasProfesor(profesor):
    materias=set([]);
    grupos_profesor=profesor.grupos.all();
    todas_materias=Materia.objects.all();
    for m in todas_materias:
        for g in m.grupos.all():
            if g.codigo_grupo in grupos_profesor:
                materias.add(m);
    return materias;



def post_list(request):
    print(str("_catasdasdas"))
    return render(request, 'temporio/index.html', {})

# Create your views here.
class Home(TemplateView):
    template_name = 'temporio/index.html'
    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        context["aaa"]="asdasasdasd";
        print(str("HOMEEEEEEEEEEEEEEEE"))
        return context


class InicioProfesor (TemplateView):
    template_name = 'temporio/profesor.html'
    def get_context_data(self, **kwargs):
        context = super(InicioProfesor, self).get_context_data(**kwargs);
        cod=self.kwargs['codigo'];
        context["codigo"]=cod;
        prfs=Profesor.objects.all().filter(codigo=cod);
        if prfs:
            context["existe"]=True;
            profesor = Profesor.objects.all().get(codigo=cod);
            context["profesor"]=profesor;
            context["materias"]=getMateriasProfesor(profesor);
        return context

class TableroProfesor(TemplateView):
    template_name = 'temporio/profesor_tablero.html'
    def get_context_data(self, **kwargs):
        context = super(TableroProfesor, self).get_context_data(**kwargs);
        cod=self.kwargs['codigo'];
        context["codigo"]=cod;
        prfs=Profesor.objects.all().filter(codigo=cod);
        if prfs:
            context["existe"]=True;
            profesor = Profesor.objects.all().get(codigo=cod);
        return context

class vistaNotificaciones(TemplateView):
    template_name = 'temporio/notificaciones_estudiante.html'
    def get_context_data(self, **kwargs):
        context = super(vistaNotificaciones, self).get_context_data(**kwargs);
        cod=self.kwargs['codigo'];
        estus=Estudiante.objects.all().filter(codigo=cod);
        if estus:
            context["existe"]=True;
            estudiante = Estudiante.objects.all().get(codigo=cod)
            # estudiante.materias.add("dasdsadas");
            if estudiante:
                context["estudiante"]=estudiante;
                context["notificaciones_propias"]=estudiante.notificaciones_propias.all();
                context["notificaciones_materias"]=getNotificacionesEstudiantes(estudiante);
        return context
