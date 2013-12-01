from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

from dajaxice.core import dajaxice_autodiscover, dajaxice_config
dajaxice_autodiscover()
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.views.generic import ListView, DetailView
from authorprofile import views
from authorprofile.models import Person, Text
from django.utils import encoding

urlpatterns = patterns('authorprofile.views',
    # Examples:
    # url(r'^$', 'authorprofile.views.home', name='home'),
    # url(r'^authorprofile/', include('authorprofile.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

    # dajax (http://django-dajaxice.readthedocs.org/en/latest/installation.html)
    url(dajaxice_config.dajaxice_url, include('dajaxice.urls')),

    # Retrieve all identified authors
    # Ensure that we are retrieving authors who have claimed texts from within AuthorClaim
    url(r'^author/?$', ListView.as_view(queryset=Person.objects.raw_query({'ids': {'$not': {'$size': 0}}}), context_object_name='personList', paginate_by=40), name='personList'),
    # url(r'^author/?$', views.personList, paginate_by=40, name='personList'),

    # For retrieving identified authors by their ACIS ID
    url(r'^author/(?P<personId>p\w+\d+)$', views.personDetail, name='personDetail'),

    # For retrieving individual, unidentified authors by their name
    url(r'^author/(?P<authorName>[\w\-\.,\s]+)$', views.authorDetail, name='authorDetail'),

    # For retrieving authors by related texts
    url(r'^author/text/(?P<textId>[\w\d\/\:\.\-_]+)$', views.textList, name='authorListByText'),

    # For retrieving texts (AJAX)
    url(r'^text/(?P<textId>[\w\d\/\:\.\-_]+)$', views.textDetail, name='textDetail')
)

urlpatterns += staticfiles_urlpatterns()
