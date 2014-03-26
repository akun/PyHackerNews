#!/usr/bin/env python


from django.conf.urls import patterns, url


urlpatterns = patterns('',
    url(r'^$', 'account.views.index', name='index'),
    url(r'^login/$', 'account.views.login', name='login'),
)
