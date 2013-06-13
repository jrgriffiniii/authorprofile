from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

from django.views.generic import ListView, DetailView
from authorprofile import views
from authorprofile.models import Person, Text

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'authorprofile.views.home', name='home'),
    # url(r'^authorprofile/', include('authorprofile.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

    # Retrieve all identified authors
    url(r'^author/?$', ListView.as_view(queryset=Person.objects.raw_query({'ids': {'$not': {'$size': 0}}}), context_object_name='acisAuthorList'), name='acisAuthorList'),

    # For retrieving individual authors
    url(r'^author/(?P<authorName>[a-zA-Z0-9\-\. ]+)$', views.authorDetail, name='authorDetail'),

    # For retrieving authors by related texts
    url(r'^author/text/(?P<textId>[a-zA-Z0-9\/:\.\-_]+)$', views.textList, name='authorListByText'),

    # For retrieving texts (AJAX)
    url(r'^text/(?P<textId>[a-zA-Z0-9\/:\.\-_]+)$', views.textDetail, name='textDetail')
)
