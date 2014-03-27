#!/usr/bin/env python


from django import forms
from django.utils.translation import ugettext_lazy as _


class AccountForm(forms.Form):

    nickname = forms.CharField(label=_(u'Nickname'), max_length=10,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    email = forms.EmailField(label=_(u'Email'), max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    about = forms.CharField(label=_(u'About'),
        widget=forms.Textarea(attrs={'class': 'form-control'})
    )
