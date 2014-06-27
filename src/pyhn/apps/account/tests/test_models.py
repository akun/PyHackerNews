#!/usr/bin/env python


from pyhn.apps.account.models import Profile
from pyhn.libs.tests.base import AnonymousTestCase


class ProfileTestCase(AnonymousTestCase):

    def test_calc_score(self):
        for profile in Profile.objects.all():
            before_score = profile.score
            profile.calc_score()
            after_score = profile.score
            self.assertNotEqual(before_score, after_score)