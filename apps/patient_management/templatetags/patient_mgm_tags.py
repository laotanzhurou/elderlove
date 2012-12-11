from django import template
from django.utils.html import conditional_escape

from account.utils import user_display


register = template.Library()
