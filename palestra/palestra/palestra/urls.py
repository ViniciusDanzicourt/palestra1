# -*- coding: utf 8 -*-
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from palestra import  settings
from inscrever import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'palestra.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('inscrever.urls'))
)+ static (settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = 'Palestras - Administração'