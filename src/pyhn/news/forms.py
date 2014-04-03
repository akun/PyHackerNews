#!/usr/bin/env python


from django import forms

from pyhn.news.models import Comment


class CommentForm(forms.Form):

    content = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control', 'rows': 6, 'cols': 60,
    }))

    def save(self, user, post):
        comment = Comment()
        comment.user = user
        comment.post = post
        comment.content = self.cleaned_data['content']
        comment.save()


class ReplyForm(CommentForm):

    def save(self, user, parent_comment):
        comment = Comment()
        comment.user = user
        comment.parent = parent_comment
        comment.post = parent_comment.post
        comment.content = self.cleaned_data['content']
        comment.save()
