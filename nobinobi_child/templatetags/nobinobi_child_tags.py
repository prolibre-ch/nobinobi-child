# Here, register is a django.template.Library instance, as before
from django import template

register = template.Library()


@register.filter
def startswith(value, arg):
    """Usage, {% if value|starts_with:"arg" %}"""
    return value.startswith(arg)
