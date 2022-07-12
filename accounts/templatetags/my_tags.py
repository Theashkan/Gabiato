from atexit import register
from django.contrib.auth.models import User

from django import template
from accounts.models import UserRelation

register = template.Library()

@register.simple_tag
def count_follower(username):
    user = User.objects.get(username=username)
    return UserRelation.objects.filter(following=user ).count()


@register.simple_tag
def count_following(username):
    user = User.objects.get(username=username)
    return UserRelation.objects.filter(follower=user ).count()