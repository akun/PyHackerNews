#!/usr/bin/env python


from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    url(r'', include('social.apps.django_app.urls', namespace='social')),
    url(r'^$', 'pyhn.news.views.index.index', name='index'),
    url(r'^news/', include('pyhn.news.urls', namespace='news')),
    url(r'^accounts/', include('pyhn.account.urls', namespace='account')),
    url(r'^admin/', include(admin.site.urls)),
)
