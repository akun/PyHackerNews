#!/usr/bin/env python


from django.conf.urls import patterns, url


urlpatterns = patterns('pyhn.account.views',
    url(r'^$', 'index', name='index'),
    url(r'^login/$', 'login', name='login'),
)
