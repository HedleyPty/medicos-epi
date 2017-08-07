from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from producto.models import Producto

# Create your views here.
def acerca(request):
	prods=Producto.objects.all()
	context = {"productos":prods}
	template = "acerca.html"
	return render(request, template, context)

@login_required
def cliente(request):
	user = request.user
	context = { "user" : user }
	template = "cliente.html"
	return render(request, template, context)
