# -*- coding: utf-8 -*
from django.db import models
from django.conf import settings

# Create your models here.
class Producto(models.Model):
	id=models.AutoField(primary_key=True)
	nombre=models.CharField(max_length=100)
	descripcion=models.CharField(max_length=1000, default="Descripción del producto")
	logo=models.CharField(max_length=200, default="")
	disponible=models.BooleanField(default=False)
	documentacion=models.CharField(max_length=200, default="URL de la documentacion")
	repos=models.CharField(max_length=200, default="", null=True, blank=True)
	app=models.CharField(max_length=200, default="URL del app")
	app_Android=models.CharField(max_length=200, default="URL del app 3")

	def __unicode__(self):
		return self.nombre
