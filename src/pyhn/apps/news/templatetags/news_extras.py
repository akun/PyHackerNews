#!/usr/bin/env python


from django import template
register = template.Library()


@register.filter
def comment_voted(comment, user):
    return comment.commentvote_set.filter(user=user).count()
