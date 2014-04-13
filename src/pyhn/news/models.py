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

        p = self.vote_set.count()
        p = p - 1 if p > 0 else 0
        timedelta = (timezone.now() - self.created_at)
        t = timedelta.days * 24 + timedelta.seconds / 3600
        g = 1.8
        score = p / (t + 2)**g
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
