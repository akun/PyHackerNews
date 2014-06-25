#!/usr/bin/env python


import json

from django.core.urlresolvers import reverse

from pyhn.libs.tests.base import AnonymousTestCase, AuthorizedTestCase
from pyhn.news.models import CommentVote, Vote


class AnonymousPostVoteTestCase(AnonymousTestCase):

    def test_vote_post_failed_if_anonymous(self):
        response = self.client.post(reverse('news:post_vote', kwargs={
            'post_id': self.POST_ID
        }))
        self.assertEqual(response.status_code, 200)
        ret = json.loads(response.content)
        self.assertEqual(100, ret['code'])


class AuthorizedPostVoteTestCase(AuthorizedTestCase):

    def test_vote_post_success(self):
        Vote.objects.all().delete()  # emtpy vote before test vote success
        response = self.client.post(reverse('news:post_vote', kwargs={
            'post_id': self.POST_ID
        }))
        self.assertEqual(response.status_code, 200)
        ret = json.loads(response.content)
        self.assertEqual(0, ret['code'])

    def test_vote_post_failed(self):
        response = self.client.post(reverse('news:post_vote', kwargs={
            'post_id': self.POST_ID
        }))
        self.assertEqual(response.status_code, 200)
        ret = json.loads(response.content)
        self.assertEqual(101, ret['code'])


class AnonymousCommentVoteTestCase(AnonymousTestCase):

    def test_vote_comment_failed_if_anonymous(self):
        response = self.client.post(reverse('news:comment_vote', kwargs={
            'comment_id': self.COMMENT_ID
        }))
        self.assertEqual(response.status_code, 200)
        ret = json.loads(response.content)
        self.assertEqual(100, ret['code'])


class AuthorizedCommentVoteTestCase(AuthorizedTestCase):

    def test_vote_comment_success(self):
        CommentVote.objects.all().delete()  # emtpy vote before test vote success
        response = self.client.post(reverse('news:comment_vote', kwargs={
            'comment_id': self.COMMENT_ID
        }))
        self.assertEqual(response.status_code, 200)
        ret = json.loads(response.content)
        self.assertEqual(0, ret['code'])

    def test_vote_comment_failed(self):
        response = self.client.post(reverse('news:comment_vote', kwargs={
            'comment_id': self.COMMENT_ID
        }))
        self.assertEqual(response.status_code, 200)
        ret = json.loads(response.content)
        self.assertEqual(101, ret['code'])
