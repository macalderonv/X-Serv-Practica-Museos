# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentarios',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('texto', models.TextField(default='')),
                ('autor', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Configuracion',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('titulo', models.TextField(default='default')),
                ('bg_color', models.CharField(max_length=32, default='blue')),
                ('tamano_ltr', models.IntegerField(default=12)),
                ('usuario', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Museos',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('nombre', models.TextField(default='')),
                ('direccion', models.TextField(default='')),
                ('descripcion', models.TextField(default='')),
                ('barrio', models.TextField(default='')),
                ('distrito', models.TextField(default='')),
                ('url', models.TextField(default='')),
                ('latitud', models.CharField(max_length=20)),
                ('longitud', models.CharField(max_length=20)),
                ('accesibilidad', models.IntegerField(default=0)),
                ('mail', models.TextField(default='')),
                ('telefono', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Seleccionados',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('fecha', models.DateField(auto_now_add=True)),
                ('museo_seleccionado', models.ForeignKey(to='museos.Museos')),
                ('usuario', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='comentarios',
            name='museo_comentado',
            field=models.ForeignKey(to='museos.Museos', default=''),
        ),
    ]
