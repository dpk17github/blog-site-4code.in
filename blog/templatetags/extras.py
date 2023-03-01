from atexit import register
from django import template

register = template.Library()

@register.filter(name="get_val")
def get_vel(dict,key):
    return dict.get(key)