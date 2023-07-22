from django import template
from movie_night.models import *
register = template.Library()

@register.simple_tag
def MyFun(User=None,Id=None):
  x= 0 if (watchListLink.objects.filter(p=User,m=Id).count() > 0) else 1
  return x
