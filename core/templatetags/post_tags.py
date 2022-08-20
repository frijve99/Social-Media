from urllib import request
from django import template
from django import core
from core.models import LikesPost
from django.contrib.auth.models import User


register = template.Library()

@register.filter(name='isLiked')
def isLiked(post_id,username):
    # username = request.user.username
    isLiked = LikesPost.objects.filter(post_id = post_id,username=username).first()
    print(isLiked)
    print(post_id)
    print(username)
    if isLiked == None:
        return False
    else:
        return True