#!/usr/bin/env python


import json

from django.core.urlresolvers import reverse

from pyhn.news.models import Vote
from pyhn.news.tests.base import AnonymousTestCase, AuthorizedTestCase


class AnonymousVoteTestCase(AnonymousTestCase):

    def test_vote_post_failed_if_anonymous(self):
        response = self.client.post(reverse('news:vote', kwargs={
            'post_id': self.POST_ID
        }))
        self.assertEqual(response.status_code, 200)
        ret = json.loads(response.content)
        self.assertEqual(100, ret['code'])


class AuthorizedVoteTestCase(AuthorizedTestCase):

    def test_vote_post_success(self):
        Vote.objects.all().delete()  # emtpy vote before test vote success
        response = self.client.post(reverse('news:vote', kwargs={
            'post_id': self.POST_ID
        }))
        self.assertEqual(response.status_code, 200)
        ret = json.loads(response.content)
        self.assertEqual(0, ret['code'])

    def test_vote_post_failed(self):
        response = self.client.post(reverse('news:vote', kwargs={
            'post_id': self.POST_ID
        }))
        self.assertEqual(response.status_code, 200)
        ret = json.loads(response.content)
        self.assertEqual(101, ret['code'])
