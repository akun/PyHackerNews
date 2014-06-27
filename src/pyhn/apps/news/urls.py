#!/usr/bin/env python


from django.conf.urls import patterns, url


urlpatterns = patterns(
    'pyhn.apps.news.views.index',
    url(r'^$', 'index', name='index'),
    url(r'^(?P<cur_page_num>\d+)/$', 'index', name='list'),
    url(r'^newest/$', 'index', {'order_by': '-created_at'}, 'newest'),
    url(r'^newest/(?P<cur_page_num>\d+)/$', 'index', {
        'order_by': '-created_at'
    }, 'newest_list'),
)
urlpatterns += patterns(
    'pyhn.apps.news.views.post',
    url(r'^submit/$', 'submit', name='submit'),
    url(r'^remove/(?P<post_id>\d+)/$', 'remove', name='post_remove'),
)
urlpatterns += patterns(
    'pyhn.apps.news.views.vote',
    url(r'^post/(?P<post_id>\d+)/vote/$', 'post_vote', name='post_vote'),
    url(
        r'^comment/(?P<comment_id>\d+)/vote/$', 'comment_vote',
        name='comment_vote'
    ),
)
urlpatterns += patterns(
    'pyhn.apps.news.views.comment',
    url(r'^post/(?P<post_id>\d+)/comment/$', 'comment_post', name='comment'),
    url(
        r'^comment/(?P<comment_id>\d+)/reply/$', 'reply_comment', name='reply'
    ),
    url(
        r'^comment/(?P<comment_id>\d+)/remove/$', 'remove',
        name='comment_remove'
    ),
)
