from django.shortcuts import render
#from . import models.Epi as epi

# Create your views here.
#from django.contrib.auth.decorators import login_required
from .models import Epi

# Create your views here.
def epi(request):
	epi=Epi.objects.all()
	context = {"Epi":epi}
	template = "epi.html"
	return render(request, template, context)
'''
def epi_(request):
    param=request.GET.get('epi', '')
    try:
        epi=epi.objects.get(id=param)
        next_ = id + 1
        prev_ = id - 1
        context={"epi":epi, "next_":next_, "prev_":prev_ }
    except:
        context={}
    template='epi.html'
    return render(request, template, context)
'''