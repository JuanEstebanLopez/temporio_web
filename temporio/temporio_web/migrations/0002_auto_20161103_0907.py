# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-03 14:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('temporio_web', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notificacion',
            name='grupo_materia',
        ),
        migrations.RemoveField(
            model_name='horario',
            name='grupo',
        ),
        migrations.AddField(
            model_name='horario',
            name='grupo',
            field=models.ManyToManyField(blank=True, related_name='grupo_horario_materia', to='temporio_web.CodigoGrupo'),
        ),
    ]