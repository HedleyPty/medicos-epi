from django.db.models import Model, CharField, ForeignKey, CASCADE
from personas.models import Estudiante

class Curso(Model):
    id=CharField(max_length=10, default="", primary_key=True)
    contenidos=CharField(max_length=10000, default="")
    ejercicios=CharField(max_length=100000,default="" )
    estudiante=ForeignKey(Estudiante, on_delete=CASCADE)
    
