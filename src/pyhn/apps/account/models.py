#!/usr/bin/env python


from django.contrib.auth.models import User as BaseUser
from django.db import models


class Profile(BaseUser):
    about = models.TextField(null=True, blank=True)
    score = models.IntegerField(default=0)

    def __unicode__(self):
        return self.username
