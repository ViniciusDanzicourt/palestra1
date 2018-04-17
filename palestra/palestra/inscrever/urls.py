from django.conf.urls import patterns, include, url
from django.contrib import admin
from views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'palestra.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^cadastro', Cadastro, name='cadastro')

)
