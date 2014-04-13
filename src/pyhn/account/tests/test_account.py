#!/usr/bin/env python


from django.core.urlresolvers import reverse

from pyhn.news.tests.base import AnonymousTestCase, AuthorizedTestCase


class AnonymousAccountTestCase(AnonymousTestCase):

    def test_login(self):
        response = self.client.get(reverse('account:login'))
        self.assertEqual(response.status_code, 200)

class AuthorizedAccountTestCase(AuthorizedTestCase):

    def test_index(self):
        response = self.client.get(reverse('account:index'))
        self.assertEqual(response.status_code, 200)
