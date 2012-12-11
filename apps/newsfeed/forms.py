import re

from django import forms
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.translation import ugettext_lazy as _, ugettext
from django.utils.http import int_to_base36

from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.models import Site

from emailconfirmation.models import EmailAddress
from timezones.forms import TimeZoneField

from account.models import Account, PasswordReset
from account.utils import perform_login, change_password

class GroupForm(forms.Form):
    
    def __init__(self, *args, **kwargs):
        self.group = kwargs.pop("group", None)
        super(GroupForm, self).__init__(*args, **kwargs)

class StatusForm(GroupForm):
    message = forms.CharField(max_length=400)
