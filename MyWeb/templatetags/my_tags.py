from django import template
from django.contrib.auth.models import User

register = template.Library()


@register.filter(name='has_group')
def has_group(user, group_name):
    return user.groups.filter(name=group_name).exists()


@register.filter(name='in_group')
def in_group(username, group_name):
    u = User.objects.get(username=username)
    return u.groups.filter(name=group_name).exists()
