#!/usr/bin/env python


from django.contrib.auth.models import User as BaseUser
from django.db import models

from pyhn.apps.news.models import CommentVote, Vote


class Profile(BaseUser):
    about = models.TextField(null=True, blank=True)
    score = models.IntegerField(default=0)

    def calc_score(self):
        """score = post vote count + comment vote count"""

        post_vote_count = Vote.objects.filter(user=self).count()
        comment_vote_count = CommentVote.objects.filter(user=self).count()
        self.score = post_vote_count + comment_vote_count
        self.save()

    def __unicode__(self):
        return self.username
