#!/usr/bin/env python


from django.core.management.base import BaseCommand, CommandError

from pyhn.apps.account.models import Profile
from pyhn.apps.news.models import Comment, CommentVote, Post, Vote, get_score


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
            score = calc_score(profile)
            profile.score = score
            profile.save()


def calc_score(profile):
    """score = post vote count + comment vote count"""

    post_vote_count = Vote.objects.filter(user=profile).count()
    comment_vote_count = CommentVote.objects.filter(user=profile).count()
    score = post_vote_count + comment_vote_count
    return score
