#!/usr/bin/env python


import json

from django import forms
from django.core.urlresolvers import reverse

from pyhn.news.models import Comment
from pyhn.news.tests.base import AnonymousTestCase, AuthorizedTestCase


class AnonymousCommentTestCase(AnonymousTestCase):

    def test_comment_get_200(self):
        response = self.client.get(reverse('news:comment', kwargs={
            'post_id': self.POST_ID,
        }))
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(0, response.context['comments'].count())

    def test_comment_get_200_no_comments(self):
        Comment.objects.all().delete()

        response = self.client.get(reverse('news:comment', kwargs={
            'post_id': self.POST_ID,
        }))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(0, response.context['comments'].count())

    def test_comment_post_failed(self):
        response = self.client.post(reverse('news:comment', kwargs={
            'post_id': self.POST_ID,
        }))
        self.assertEqual(response.status_code, 302)
        self.assertTrue('?next=' in response.url)


class AuthorizedCommentTestCase(AuthorizedTestCase):

    def test_comment_get_200(self):
        response = self.client.get(reverse('news:comment', kwargs={
            'post_id': self.POST_ID,
        }))
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(0, response.context['comments'].count())

    def test_comment_get_200_no_comments(self):
        Comment.objects.all().delete()

        response = self.client.get(reverse('news:comment', kwargs={
            'post_id': self.POST_ID,
        }))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(0, response.context['comments'].count())

    def test_comment_post_success(self):
        content = 'xxxx'
        response = self.client.post(reverse('news:comment', kwargs={
            'post_id': self.POST_ID,
        }), {'content': content})
        self.assertEqual(response.status_code, 302)
        comment = Comment.objects.get(post_id=self.POST_ID, content=content)
        self.assertEqual(content, comment.content)

    def test_comment_post_failed(self):
        response = self.client.post(reverse('news:comment', kwargs={
            'post_id': self.POST_ID,
        }))
        self.assertEqual(response.status_code, 200)
        self.assertFormError(
            response, 'comment_form', 'content',
            forms.CharField.default_error_messages['required']
        )

    def test_remove(self):
        for comment in Comment.objects.all():
            response = self.client.post(reverse('news:comment_remove', kwargs={
                'comment_id': comment.id
            }))
            self.assertEqual(response.status_code, 200)
            ret = json.loads(response.content)
            self.assertEqual(0, ret['code'])


class AnonymousReplyTestCase(AnonymousTestCase):

    def test_reply_post_failed_if_anonymous(self):
        response = self.client.post(reverse('news:reply', kwargs={
            'comment_id': self.COMMENT_ID,
        }))
        self.assertEqual(response.status_code, 200)
        ret = json.loads(response.content)
        self.assertEqual(100, ret['code'])


class AuthorizedReplyTestCase(AuthorizedTestCase):

    def test_reply_post_success(self):
        content = 'yyyy'
        response = self.client.post(reverse('news:reply', kwargs={
            'comment_id': self.COMMENT_ID,
        }), {'content': content})
        self.assertEqual(response.status_code, 200)
        ret = json.loads(response.content)
        self.assertEqual(0, ret['code'])
        comment = Comment.objects.get(
            parent__id=self.COMMENT_ID, content=content
        )
        self.assertEqual(content, comment.content)

    def test_reply_post_failed(self):
        response = self.client.post(reverse('news:reply', kwargs={
            'comment_id': self.COMMENT_ID,
        }))
        self.assertEqual(response.status_code, 200)
        ret = json.loads(response.content)
        self.assertEqual(101, ret['code'])
        self.assertEqual(
            forms.CharField.default_error_messages['required'],
            ret['result']['errors']['content'][0]
        )
