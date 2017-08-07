from django.contrib import admin
from .models import Estudiante, Profesor
# Register your models here.
class EstAdmin(admin.ModelAdmin):
	class Meta:
		model=Estudiante
class ProfAdmin(admin.ModelAdmin):
	class Meta:
		model=Profesor


admin.site.register(Estudiante, EstAdmin)
admin.site.register(Profesor, ProfAdmin)
