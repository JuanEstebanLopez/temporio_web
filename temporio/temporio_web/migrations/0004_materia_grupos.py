# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-05 15:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('temporio_web', '0003_auto_20161103_1716'),
    ]

    operations = [
        migrations.AddField(
            model_name='materia',
            name='grupos',
            field=models.ManyToManyField(blank=True, null=True, related_name='grupos_materia', to='temporio_web.Grupo'),
        ),
    ]
