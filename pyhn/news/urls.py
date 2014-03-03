#!/usr/bin/env python


from django.conf.urls import patterns, url

from news import views


urlpatterns = patterns('',
    url(r'^$', views.index, name='news_index'),
    url(r'^(?P<cur_page_num>\d+)/$', views.index, name='news_list'),
)
