from django.db.models import Model, CharField

# Create your models here.
class Persona(Model):
    primer_nombre=CharField(max_length=30)
    segundo_nombre=CharField(max_length=30, null=True)
    primer_apellido=CharField(max_length=30)
    segundo_apellido=CharField(max_length=30, null=True)
    apellido_de_casada=CharField(max_length=30,null=True)
    cedula=CharField(max_length=30, null=True)
class Estudiante(Persona):
    notas=CharField(max_length=3000)
class Profesor(Persona):
    pass
