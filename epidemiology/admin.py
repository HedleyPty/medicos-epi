from django.contrib import admin
from .models import Epi
class EpiAdmin(admin.ModelAdmin):
    class Meta:
        model=Epi
admin.site.register(Epi, EpiAdmin)

# Register your models here.
