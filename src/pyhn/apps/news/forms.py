#!/usr/bin/env python


from django import forms
from django.utils.translation import ugettext_lazy as _

from pyhn.apps.news.models import Comment, Post


class PostForm(forms.Form):
    title = forms.CharField(
        label=_('Title'), max_length=200,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    url = forms.URLField(
        label=_('URL'), required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    content = forms.CharField(
        label=_('Content'), required=False, widget=forms.Textarea(
            attrs={'class': 'form-control', 'rows': 6, 'cols': 60}
        )
    )

    def save(self, user):
        post = Post()
        post.user = user
        post.title = self.cleaned_data['title']
        post.url = self.cleaned_data['url']
        post.content = self.cleaned_data['content']
        post.save()


class CommentForm(forms.Form):

    content = forms.CharField(
        widget=forms.Textarea(
            attrs={'class': 'form-control', 'rows': 6, 'cols': 60}
        )
    )

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
