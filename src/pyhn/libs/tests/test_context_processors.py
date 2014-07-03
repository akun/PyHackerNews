#!/usr/bin/env python
# coding=utf-8


from django.test import TestCase

from pyhn.libs import context_processors


class ContextProcessorsTestCase(TestCase):

    def test_pyhn_info_if_default(self):
        context = context_processors.pyhn_info(self.client.request)
        self.assertEqual('', context['PYHN_TITLE'])
        self.assertEqual('', context['PYHN_COPYRIGHT'])

    def test_pyhn_info_if_edit_settings(self):
        from django.conf import settings
        title = 'test_title'
        copyright = 'test_copyright'
        settings.PYHN_TITLE = title
        settings.PYHN_COPYRIGHT = copyright

        context = context_processors.pyhn_info(self.client.request)
        self.assertEqual(title, context['PYHN_TITLE'])
        self.assertEqual(copyright, context['PYHN_COPYRIGHT'])

        settings.PYHN_TITLE = ''
        settings.PYHN_COPYRIGHT = ''
