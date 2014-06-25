#!/usr/bin/env python


from django import forms
from django.core.urlresolvers import reverse
from django.core.validators import EmailValidator

from pyhn.account.models import Profile
from pyhn.libs.tests.base import AnonymousTestCase, AuthorizedTestCase


class AnonymousAccountTestCase(AnonymousTestCase):

    def test_login(self):
        response = self.client.get(reverse('account:login'))
        self.assertEqual(response.status_code, 200)

    def test_user_profile(self):
        for profile in Profile.objects.all():
            response = self.client.get(reverse('profile', kwargs={
                'user_id': profile.id
            }))
            self.assertEqual(response.status_code, 200)


class AuthorizedAccountTestCase(AuthorizedTestCase):

    def test_index_get_200(self):
        response = self.client.get(reverse('account:index'))
        self.assertEqual(response.status_code, 200)

    def test_index_success(self):
        response = self.client.post(reverse('account:index'), {
            'username': 'username',
            'email': 'username@example.com',
            'about': 'somebody'
        })
        self.assertEqual(response.status_code, 302)

    def test_index_failed_if_username_empty(self):
        response = self.client.post(reverse('account:index'), {
            'username': '',
        })
        self.assertEqual(response.status_code, 200)
        self.assertFormError(
            response, 'form', 'username',
            forms.CharField.default_error_messages['required']
        )

    def test_index_failed_if_email(self):
        response = self.client.post(reverse('account:index'), {
            'username': 'username',
            'email': 'username$example.com'
        })
        self.assertEqual(response.status_code, 200)
        self.assertFormError(response, 'form', 'email', EmailValidator.message)
