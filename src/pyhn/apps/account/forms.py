#!/usr/bin/env python


from django import forms
from django.utils.translation import ugettext_lazy as _

from pyhn.apps.account.models import Profile


class AccountForm(forms.Form):

    username = forms.CharField(
        label=_(u'Username'), max_length=10,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    email = forms.EmailField(
        label=_(u'Email'), max_length=50, required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    about = forms.CharField(
        label=_(u'About'), required=False,
        widget=forms.Textarea(attrs={'class': 'form-control'})
    )

    def save(self, user):
        profile = Profile(user_ptr=user)
        profile.username = self.cleaned_data['username']
        profile.email = self.cleaned_data['email']
        profile.about = self.cleaned_data['about']
        profile.save()
