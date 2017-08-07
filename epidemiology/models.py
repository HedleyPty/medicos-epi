from __future__ import unicode_literals
#from random import randint
from django.db import models

# Create your models here.
class Epi(models.Model):
	id=models.AutoField(primary_key=True)
	#Informacion
	titl=models.CharField(max_length=100, default="Titulo predeterminado")
	#nombre=models.CharField(max_length=24, default="Titulo predeterminado")
	texto=models.CharField(max_length=10000, default="Texto amigable")
	imagenes=models.CharField(max_length=200, default="")
	#Preguntas
	encabezado_pregunta=models.CharField(max_length=10000, default="Texto amigable")
	repuesta_correcta=models.CharField(max_length=20, default="Texto amigable")
	distractor_1=models.CharField(max_length=20, default="Texto amigable")
	distractor_2=models.CharField(max_length=20, default="Texto amigable")
	distractor_3=models.CharField(max_length=20, default="Texto amigable")

	def __unicode__(self):
	    return self.titl
