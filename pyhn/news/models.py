#!/usr/bin/env python


from django.db import models


class Post(models.Model):
    user = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    url = models.URLField(null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
