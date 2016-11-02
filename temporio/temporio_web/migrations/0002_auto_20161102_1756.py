# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-02 22:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('temporio_web', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CodigoGrupo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=128)),
            ],
        ),
        migrations.RemoveField(
            model_name='estudiante',
            name='apuntes_compartidos',
        ),
        migrations.RemoveField(
            model_name='estudiante',
            name='apuntes_favoritos',
        ),
        migrations.RemoveField(
            model_name='estudiante',
            name='materias',
        ),
        migrations.RemoveField(
            model_name='estudiante',
            name='notificaciones_propias',
        ),
        migrations.AddField(
            model_name='notificacion',
            name='str_fecha',
            field=models.CharField(default='ooo', max_length=128),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='grupo',
            name='codigo_grupo',
            field=models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to='temporio_web.CodigoGrupo'),
        ),
        migrations.AlterField(
            model_name='notificacion',
            name='estado',
            field=models.IntegerField(default=1),
        ),
    ]