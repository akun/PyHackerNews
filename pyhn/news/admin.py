#!/usr/bin/env python


from django.contrib import admin
from news.models import Post, Vote


admin.site.register(Post)
admin.site.register(Vote)
