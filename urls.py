from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

from django.views.generic import ListView, DetailView
from authorprofile.models import Person

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'authorprofile.views.home', name='home'),
    # url(r'^authorprofile/', include('authorprofile.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

    url(r'^$', ListView.as_view(queryset=Person.objects.raw_query({'ids': {'$size': 1}}), context_object_name='acisAuthorList'), name='acisAuthorList'),
    url(r'^$', DetailView.as_view(queryset=Person.objects.raw_query({'ids': {'$size': 0}}), context_object_name='acisAuthorDetail'), name='acisAuthorDetail'),
)
