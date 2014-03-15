#!/usr/bin/env python


from django.conf.urls import patterns, url


urlpatterns = patterns('',
    url(r'^$', 'news.views.index', name='news_index'),
    url(r'^(?P<cur_page_num>\d+)/$', 'news.views.index', name='news_list'),
)
