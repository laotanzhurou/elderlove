import datetime

import datetime
import sys# sys stands for System-specific parameters and functions

from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import get_language_from_request, ugettext_lazy as _

from django.contrib.auth.models import User, AnonymousUser
from timezones.fields import TimeZoneField


# Create your models here.

class Status(models.Model):
    user = models.ForeignKey(User, related_name='status_poster')
    message = models.CharField(_("post"), max_length=400, null=False, blank=False)
    post_time = models.DateTimeField(_('post_time'), default=datetime.datetime.now)

class Mood(models.Model):
    user = models.ForeignKey(User, related_name='mood_poster')
    mood_message = models.CharField(_("post"), max_length=400, null=False, blank=False)
    post_time = models.DateTimeField(_('post_time'), default=datetime.datetime.now)