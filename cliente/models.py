from __future__ import unicode_literals
from django.db import models
from django.conf import settings
from allauth.account.signals import user_logged_in,user_signed_up
import stripe

# Create your models here.
class cliente(models.Model):
	nombre=models.CharField(max_length=1200)
	direccion=models.TextField(default="")
	descripcion=models.TextField(default="")
	user=models.OneToOneField(settings.AUTH_USER_MODEL, null=True, blank=True)

	def __unicode__(self):
		return self.nombre 

class clienteStripe(models.Model):
	user=models.OneToOneField(settings.AUTH_USER_MODEL)
	stripe_id = models.CharField(max_length=200, null=True, blank=True)
		
	def __unicode__(self):
		pass
		if self.stripe_id:
			return self.stripe_id
		else:
			return self.usuario.username

def stripeCallback(sender,request, user, **kwargs):
	cuenta_usuario_Stripe, id_creada=clienteStripe.objects.get_or_create(user=user)
	if id_creada:
		print "created for %s"%(user.username)
	if cuenta_usuario_Stripe.stripe_id == None or cuenta_usuario_Stripe.stripe_id=="":
		new_stripe_id = stripe.Customer.create(email=user.email)
		cuenta_usuario_Stripe.stripe_id = new_stripe_id['id']
		cuenta_usuario_Stripe.save()

def clienteCallback(sender,request, user, **kwargs): 
	usuarioCliente, Cliente_creado=cliente.objects.get_or_create(usuario=user)
	if Cliente_creado:
		usuarioCliente.nombre= user.username	
		usuarioCliente.save()


user_logged_in.connect(stripeCallback)
user_signed_up.connect(stripeCallback)
user_signed_up.connect(clienteCallback)
