#!/usr/bin/env python


from django.core.management import call_command

from pyhn.apps.account.models import Profile
from pyhn.apps.news.models import Comment, Post, get_score
from pyhn.libs.tests.base import AnonymousTestCase as TestCase
from pyhn.management.commands.score import calc_score


class CommandsTestCase(TestCase):

    def test_command_score(self):

        score_info = {
            Post: {},
            Comment: {},
            Profile: {},
        }

        for obj_class in score_info:
            for obj in getattr(obj_class, 'objects').all():
                score_info[obj_class][obj.id] = obj.score

        call_command('score')

        for obj_class in score_info:
            for obj in getattr(obj_class, 'objects').all():
                self.assertNotEqual(score_info[obj_class][obj.id], obj.score)

    def test_calc_score(self):
        for profile in Profile.objects.all():
            score = calc_score(profile)
            self.assertNotEqual(0, score)
