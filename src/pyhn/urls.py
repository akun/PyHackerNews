#!/usr/bin/env python


from django.conf.urls import patterns, include, url


urlpatterns = patterns(
    '',
    url(r'', include('social.apps.django_app.urls', namespace='social')),
    url(r'^$', 'pyhn.apps.news.views.index.index', name='index'),
    url(r'^news/', include('pyhn.apps.news.urls', namespace='news')),
    url(r'^accounts/', include('pyhn.apps.account.urls', namespace='account')),
    url(
        r'^user/(?P<user_id>\d+)/', 'pyhn.apps.account.views.user_profile',
        name='profile'
    ),
)
