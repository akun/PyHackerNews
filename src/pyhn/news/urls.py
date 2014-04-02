#!/usr/bin/env python


from django.conf.urls import patterns, url


urlpatterns = patterns('pyhn.news.views.index',
    url(r'^$', 'index', name='index'),
    url(r'^(?P<cur_page_num>\d+)/$', 'index', name='list'),
)
urlpatterns += patterns('pyhn.news.views.vote',
    url(r'^vote/(?P<post_id>\d+)$', 'vote', name='vote'),
)
urlpatterns += patterns('pyhn.news.views.comment',
    url(r'^(?P<post_id>\d+)/comment/$', 'comment', name='comment'),
)
