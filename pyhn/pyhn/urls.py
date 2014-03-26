#!/usr/bin/env python


from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    url(r'', include('social.apps.django_app.urls', namespace='social')),
    url(r'^$', 'news.views.index', name='index'),
    url(r'^news/', include('news.urls', namespace='news')),
    url(r'^accounts/', include('account.urls', namespace='account')),
    url(r'^admin/', include(admin.site.urls)),
)
