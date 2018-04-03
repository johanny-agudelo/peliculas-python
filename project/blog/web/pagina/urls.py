from django.conf.urls import include, url
from django.contrib import admin
from pagina.views import index


urlpatterns = [
    

     url(r'^admin/', include(admin.site.urls)),
     url(r'^post/', include('pagina.urls', namespace='pagina')),
     url(r'^index/', index, name='index')
    
]#+static(settings.STATIC_URL,documento_root=settings.STATIC_ROOT)
