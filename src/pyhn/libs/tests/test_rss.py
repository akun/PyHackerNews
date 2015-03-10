#!/usr/bin/env python

from django import forms
from django.core.urlresolvers import reverse
from django.core.validators import EmailValidator

from pyhn.apps.account.models import Profile
from pyhn.libs.tests.base import AnonymousTestCase as TestCase


class RssTestCase(TestCase):

    def test_rss(self):
        response = self.client.get(reverse('rss'))
        self.assertEqual(response.status_code, 200)
