#!/usr/bin/env python


from django.core.management.base import BaseCommand, CommandError

from pyhn.apps.account.models import Profile
from pyhn.apps.news.models import Comment, Post, get_score


class Command(BaseCommand):

    help = 'Calculate score for post, comment, profile'

    def handle(self, *args, **options):

        for post in Post.objects.all():
            score = get_score(post.vote_set.count(), post.created_at)
            post.score = score
            post.save()

        for comment in Comment.objects.all():
            score = get_score(comment.commentvote_set.count(), comment.created_at)
            comment.score = score
            comment.save()

        for profile in Profile.objects.all():
            profile.calc_score()
