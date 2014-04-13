#!/usr/bin/env python


from django.core.urlresolvers import reverse
from django.test import TestCase


class ListTestCase(TestCase):

    def test_list_default(self):
        response = self.client.get(reverse('news:index'))
        self.assertEqual(response.status_code, 200)

    def test_list_with_paginator(self):
        response = self.client.get(reverse('news:list', kwargs={
            'cur_page_num': 1
        }))
        self.assertEqual(response.status_code, 200)

    def test_newest_list_default(self):
        response = self.client.get(reverse('news:newest'))
        self.assertEqual(response.status_code, 200)

    def test_newest_list_with_paginator(self):
        response = self.client.get(reverse('news:newest_list', kwargs={
            'cur_page_num': 1
        }))
        self.assertEqual(response.status_code, 200)
