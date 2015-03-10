#!/usr/bin/env python


from django.conf import settings
from django.contrib.syndication.views import Feed

from pyhn.apps.news.models import Post


class NewsFeed(Feed):
    title = settings.PYHN_RSS_TITLE
    link = '/rss/'
    description = settings.PYHN_RSS_DESCRIPTION

    def items(self):
        return Post.objects.order_by('-created_at')[:settings.PYHN_RSS_SIZE]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        for i in ('url', 'content'):
            description = getattr(item, i)
            if description:
                return description

    def item_link(self, item):
        return item.url

    def item_author_name(self, item):
        return item.user.username
