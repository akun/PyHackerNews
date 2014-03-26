#!/usr/bin/env python


from django.conf.urls import patterns, url


urlpatterns = patterns('pyhn.news.views',
    url(r'^$', 'index', name='index'),
    url(r'^(?P<cur_page_num>\d+)/$', 'index', name='list'),
    url(r'^vote/(?P<post_id>\d+)$', 'vote', name='vote'),
    url(r'^(?P<post_id>\d+)/comment/$', 'comment', name='comment'),
)
