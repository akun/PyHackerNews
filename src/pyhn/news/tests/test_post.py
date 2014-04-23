#!/usr/bin/env python


import json

from django import forms
from django.core.urlresolvers import reverse

from pyhn.news.models import Post
from pyhn.news.tests.base import AuthorizedTestCase


class PostTestCase(AuthorizedTestCase):

    def test_submit_get_200(self):
        response = self.client.get(reverse('news:submit'))
        self.assertEqual(response.status_code, 200)

    def test_submit_post_success(self):
        title = 'SubmitExample'
        url = 'http://www.example.com/submit.html'
        response = self.client.post(reverse('news:submit'), data={
            'title': title, 'url': url,
        })
        self.assertEqual(response.status_code, 302)
        post = Post.objects.get(url=url)
        self.assertEqual(title, post.title)

    def test_submit_post_failed_if_title_is_empty(self):
        response = self.client.post(reverse('news:submit'))
        self.assertEqual(response.status_code, 200)
        self.assertFormError(
            response, 'form', 'title',
            forms.CharField.default_error_messages['required']
        )

    def test_remove_post(self):
        for post in Post.objects.all():
            response = self.client.post(reverse('news:post_remove', kwargs={
                'post_id': post.id
            }))
            self.assertEqual(response.status_code, 200)
            ret = json.loads(response.content)
            self.assertEqual(0, ret['code'])
