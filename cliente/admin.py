from django.contrib import admin
from .models import cliente, clienteStripe

# Register your models here.
class clienteAdmin(admin.ModelAdmin):
	class Meta:
		model=cliente

admin.site.register(cliente, clienteAdmin)

class clienteStripeAdmin(admin.ModelAdmin):
	class Meta:
		model=clienteStripe

admin.site.register(clienteStripe, clienteStripeAdmin)
