#!/usr/bin/env python


from django.conf.urls import patterns, url


urlpatterns = patterns(
    'pyhn.apps.account.views',
    url(r'^$', 'index', name='index'),
    url(r'^login/$', 'login', name='login'),
)
urlpatterns += patterns(
    'django.contrib.auth.views',
    url(r'^logout/$', 'logout', {'next_page': '/'}, 'logout'),
)
