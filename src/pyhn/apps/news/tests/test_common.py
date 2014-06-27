#!/usr/bin/env python


from django.test import TestCase

from pyhn.apps.news.views.common import get_paged_object


class PaginatorTestCase(TestCase):

    def test_error_paginator_if_value_error(self):
        test_list = range(60)
        num_per_page = 30
        paged_object = get_paged_object(test_list, 'a', num_per_page)
        self.assertEqual(test_list[:num_per_page], paged_object.object_list)

    def test_error_paginator_if_page_error(self):
        test_list = range(60)
        num_per_page = 30
        for cur_page_num in (-1, 99):
            paged_object = get_paged_object(
                test_list, cur_page_num, num_per_page
            )
            self.assertEqual(
                test_list[-num_per_page:], paged_object.object_list
            )
