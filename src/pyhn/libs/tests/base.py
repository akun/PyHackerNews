#!/usr/bin/env python


from django.test import TestCase
from django.test.client import Client


class AnonymousTestCase(TestCase):

    fixtures = [
        'user.json',
        'profile.json',
        'post.json',
        'vote.json',
        'comment.json',
        'comment_vote.json'
    ]

    POST_ID = 9527
    COMMENT_ID = 1


class AuthorizedTestCase(AnonymousTestCase):

    def setUp(self):
        self.client = Client(enforce_csrf_checks=False)
        self.client.login(username='admin', password='admin')

    def tearDown(self):
        self.client.logout()
