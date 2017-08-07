from django.shortcuts import render
from .models import Producto

# Create your views here.
def home(request):
    prods=Producto.objects.all()
    context={"productos": prods}
    template='home.html'
    return render(request, template, context)

def cv(request):
    context={"English":False}
    template='CV.html'
    return render(request, template, context)

def cv_en(request):
    context={"English":True}
    template='CVen.html'
    return render(request, template, context)


def app(request):
    param=request.GET.get('app', '')
    try:
        app=Producto.objects.get(nombre=param)
        context={"app":app}
    except:
        context={}
    template='app.html'
    return render(request, template, context)
