from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [

	
	url(r'^planning/$', 'planning.views.home' ,name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^display/', 'planning.views.plan', name='planning'),
    url(r'^$', 'planning.views.ConnexionNovy', name='ConnexionNovy'),

]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)