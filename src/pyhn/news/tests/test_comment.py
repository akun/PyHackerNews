#!/usr/bin/env python


from django import forms
from django.core.urlresolvers import reverse
from django.test import TestCase
from django.test.client import Client

from pyhn.news.models import Comment


POST_ID = 9527


class CommentTestCase(TestCase):

    fixtures = ['user.json', 'post.json', 'comment.json']

    def setUp(self):
        self.client = Client(enforce_csrf_checks=False)
        self.client.login(username='admin', password='admin')

    def tearDown(self):
        self.client.logout()

    def test_comment_get_200(self):
        response = self.client.get(reverse('news:comment', kwargs={
            'post_id': POST_ID
        }))
        self.assertEqual(response.status_code, 200)

    def test_comment_post_success(self):
        content = 'xxxx'
        response = self.client.post(reverse('news:comment', kwargs={
            'post_id': POST_ID
        }), {'content': content})
        self.assertEqual(response.status_code, 302)
        comment = Comment.objects.get(post_id=POST_ID, content=content)
        self.assertEqual(content, comment.content)

    def test_comment_post_failed(self):
        response = self.client.post(reverse('news:comment', kwargs={
            'post_id': POST_ID
        }))
        self.assertEqual(response.status_code, 200)
        self.assertFormError(
            response, 'form', 'content',
            forms.CharField.default_error_messages['required']
        )
