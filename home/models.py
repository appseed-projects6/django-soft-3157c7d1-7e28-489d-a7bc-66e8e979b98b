# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Forms(models.Model):

    #__Forms_FIELDS__
    form = models.CharField(max_length=255, null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    available = models.CharField(max_length=255, null=True, blank=True)

    #__Forms_FIELDS__END

    class Meta:
        verbose_name        = _("Forms")
        verbose_name_plural = _("Forms")


class Users(models.Model):

    #__Users_FIELDS__
    username = models.CharField(max_length=255, null=True, blank=True)
    full name = models.CharField(max_length=255, null=True, blank=True)
    bio = models.CharField(max_length=255, null=True, blank=True)

    #__Users_FIELDS__END

    class Meta:
        verbose_name        = _("Users")
        verbose_name_plural = _("Users")



#__MODELS__END
