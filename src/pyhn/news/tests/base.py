#!/usr/bin/env python


from django.test import TestCase
from django.test.client import Client


class AnonymousTestCase(TestCase):

    fixtures = ['user.json', 'post.json', 'comment.json']


class AuthorizedTestCase(AnonymousTestCase):

    def setUp(self):
        self.client = Client(enforce_csrf_checks=False)
        self.client.login(username='admin', password='admin')

    def tearDown(self):
        self.client.logout()
