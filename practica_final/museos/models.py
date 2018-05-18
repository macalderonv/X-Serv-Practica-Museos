# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Museos(models.Model):
    nombre = models.TextField(default="")
    direccion = models.TextField(default="")
    descripcion = models.TextField(default="")
    barrio = models.TextField(default="")
    distrito = models.TextField(default="")
    url = models.TextField(default="")
    latitud = models.CharField(max_length=20)
    longitud = models.CharField(max_length=20)
    accesibilidad = models.IntegerField(default=0)
    mail = models.TextField(default="")
    telefono = models.CharField(max_length=20)
    def __unicode__ (self):
        return (self.nombre)

class Configuracion(models.Model):
    usuario = models.ForeignKey(User)
    titulo = models.TextField(default="default")
    bg_color = models.CharField(default="blue", max_length=32)
    tamano_ltr = models.IntegerField(default=12)
    def __unicode__ (self):
        return unicode(self.usuario)

class Comentarios(models.Model):
    texto = models.TextField(default="")
    museo_comentado = models.ForeignKey('Museos', default="")
    autor = models.ForeignKey(User)
    def __unicode__(self):
        return unicode(self.autor)

class Seleccionados(models.Model):
    museo_seleccionado = models.ForeignKey('Museos')
    usuario = models.ForeignKey(User)
    fecha = models.DateField(auto_now_add=True)
    def __unicode__ (self):
        return unicode(self.museo_seleccionado)
