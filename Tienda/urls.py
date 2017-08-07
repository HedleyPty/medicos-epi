from django.conf.urls import include, url
from django.contrib import admin
from producto import views as p
#from cliente import views as c
#from checkout import views as ch
#from epidemiology import views as epi
from django.conf import settings
from django.conf.urls.static import static
#from allauth import urls
#import os
admin.autodiscover()

urlpatterns = [
    url(r'^cv_en/', p.cv_en, name="cv_en"),
    url(r'^moste/', admin.site.urls),
    #url(r'^cliente/', c.cliente, name="cliente"),
    #url(r'^acerca/', c.acerca, name="acerca"),
   # url(r'^app/\?app=.*', p.app, name="app"),
    #url(r'^checkout/', ch.checkout, name="checkout"),
    #url(r'^accounts/', include('allauth.urls')),
  #  url(r'^cv/?', p.cv, name="cv"),
  #      url(r'.*', p.cv, name="cv"),

    #url(r'^epi/\?id=.*', epi.epi, name="epi"),
    url(r'.*', p.cv, name="cv"),
 ]

urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL,  document_root = settings.MEDIA_ROOT)

