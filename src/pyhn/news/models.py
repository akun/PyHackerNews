#!/usr/bin/env python


from django.db import models
from django.utils import timezone


class Post(models.Model):
    user = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    url = models.URLField(null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    score = models.FloatField(default=0.0)

    class Meta:
        ordering = ['-score', '-created_at']

    def __unicode__(self):
        return self.title

    def vote(self, user):
        """
        ref: http://www.ruanyifeng.com/blog/2012/02/ranking_algorithm_hacker_news.html
        """

        Vote.objects.create(user=user, post=self)

        score = get_score(self.vote_set.count(), self.created_at)
        self.score = score
        self.save()

        return score


class Vote(models.Model):
    user = models.ForeignKey('auth.User')
    post = models.ForeignKey('Post')

    def __unicode__(self):
        return '%s, %s' % (self.user.username, self.post.title)


class Comment(models.Model):
    user = models.ForeignKey('auth.User')
    parent = models.ForeignKey('self', null=True, blank=True)
    post = models.ForeignKey('Post')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    score = models.FloatField(default=0.0)

    class Meta:
        ordering = ['-score', '-created_at']

    def __unicode__(self):
        return '%s, %s' % (self.user, self.post)

    def vote(self, user):
        CommentVote.objects.create(user=user, comment=self)

        score = get_score(self.commentvote_set.count(), self.created_at)
        self.score = score
        self.save()

        return score


class CommentVote(models.Model):
    user = models.ForeignKey('auth.User')
    comment = models.ForeignKey('Comment')

    def __unicode__(self):
        return '%s, %s' % (self.user.username, self.comment.content[:10])


def get_score(param_count, created_at):
    param_count = param_count - 1 if param_count > 0 else 0
    timedelta = (timezone.now() - created_at)
    param_time = timedelta.days * 24 + timedelta.seconds / 3600
    param_base = 1.8
    score = param_count / (param_time + 2)**param_base
    return score
