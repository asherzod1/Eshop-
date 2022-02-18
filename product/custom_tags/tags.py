from django import template

register = template.Library()

@register.simple_tag('add')
def add(value, v1):
    return value + v1