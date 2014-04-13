#!/usr/bin/env python


from django.conf.urls import patterns, url


urlpatterns = patterns(
    'pyhn.news.views.index',
    url(r'^$', 'index', name='index'),
    url(r'^(?P<cur_page_num>\d+)/$', 'index', name='list'),
    url(r'^newest/$', 'index', {'order_by': '-created_at'}, 'newest'),
    url(r'^newest/(?P<cur_page_num>\d+)/$', 'index', {
        'order_by': '-created_at'
    }, 'newest_list'),
)
urlpatterns += patterns(
    'pyhn.news.views.post',
    url(r'^submit/$', 'submit', name='submit'),
)
urlpatterns += patterns(
    'pyhn.news.views.vote',
    url(r'^post/(?P<post_id>\d+)/vote/$', 'vote', name='vote'),
)
urlpatterns += patterns(
    'pyhn.news.views.comment',
    url(r'^post/(?P<post_id>\d+)/comment/$', 'comment_post', name='comment'),
    url(
        r'^comment/(?P<comment_id>\d+)/reply/$', 'reply_comment', name='reply'
    ),
)
