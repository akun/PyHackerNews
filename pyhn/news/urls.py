#!/usr/bin/env python


from django.conf.urls import patterns, url


urlpatterns = patterns('',
    url(r'^$', 'news.views.index', name='index'),
    url(r'^(?P<cur_page_num>\d+)/$', 'news.views.index', name='list'),
    url(r'^vote/(?P<post_id>\d+)$', 'news.views.vote', name='vote'),
    url(r'^comment/(?P<post_id>\d+)$', 'news.views.comment', name='comment'),
)
