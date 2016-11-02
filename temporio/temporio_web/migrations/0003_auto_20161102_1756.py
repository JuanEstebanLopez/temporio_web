# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-02 22:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('temporio_web', '0002_auto_20161102_1756'),
    ]

    operations = [
        migrations.AddField(
            model_name='estudiante',
            name='apuntes_compartidos',
            field=models.ManyToManyField(blank=True, related_name='compartidos', to='temporio_web.Apunte'),
        ),
        migrations.AddField(
            model_name='estudiante',
            name='apuntes_favoritos',
            field=models.ManyToManyField(blank=True, related_name='favoritos', to='temporio_web.Apunte'),
        ),
        migrations.AddField(
            model_name='estudiante',
            name='materias',
            field=models.ManyToManyField(blank=True, to='temporio_web.CodigoGrupo'),
        ),
        migrations.AddField(
            model_name='estudiante',
            name='notificaciones_propias',
            field=models.ManyToManyField(blank=True, related_name='notificaciones', to='temporio_web.Notificacion'),
        ),
    ]
