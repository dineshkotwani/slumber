from django.conf.urls import patterns, include, url
from teemo.auth.views import *
from teemo.tprofile.views import *
from django.views.generic import TemplateView
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',

    url(r'^$',TemplateView.as_view(template_name='home.html')),
    url(r'^about/$', TemplateView.as_view(template_name='about.html')),
    url(r'^pricing/$', TemplateView.as_view(template_name='pricing.html')),
    url(r'^faq/$', TemplateView.as_view(template_name='faq.html')),    

    url(r'^auth/$', auth),
    url(r'^register/$', register),
    
    url(r'^admin/', include(admin.site.urls)),
)
