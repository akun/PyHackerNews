#!/usr/bin/env python


from django.conf.urls import patterns, url


urlpatterns = patterns('pyhn.news.views.index',
    url(r'^$', 'index', name='index'),
    url(r'^(?P<cur_page_num>\d+)/$', 'index', name='list'),
)
urlpatterns += patterns('pyhn.news.views.vote',
    url(r'^post/(?P<post_id>\d+)/vote/$', 'vote', name='vote'),
)
urlpatterns += patterns('pyhn.news.views.comment',
    url(r'^post/(?P<post_id>\d+)/comment/$', 'comment', name='comment'),
    url(r'^comment/(?P<comment_id>\d+)/reply/$', 'reply', name='reply'),
)
