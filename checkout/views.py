from django.shortcuts import render
from django.conf import settings
import stripe
from django.contrib.auth.decorators import login_required
# Create your views here.

stripe.api_key = settings.STRIPE_SECRET_KEY
@login_required
def checkout(request):
	publishKey=settings.STRIPE_PUBLISHABLE_KEY
	cliente_id= request.user.clientestripe.stripe_id
        if request.method=="POST":
		token=request.POST["stripeToken"]
		try:
			cliente=stripe.Customer.create(cliente_id, source=token)
			cliente.id=cliente_id
			charge = stripe.Charge.create(
			amount= 1000, # amount in cents, again
			currency="sek",
			source=cliente_id,
			description="Example charge")
		except stripe.error.CardError, e:
		  # The card has been declined
			pass
        context = {'publishKey':publishKey }
        template = "checkout.html"
        return render(request, template, context)




