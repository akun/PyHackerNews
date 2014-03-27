#!/usr/bin/env python


from django.contrib import admin
from pyhn.news.models import Comment, Post, Vote


admin.site.register(Comment)
admin.site.register(Post)
admin.site.register(Vote)
