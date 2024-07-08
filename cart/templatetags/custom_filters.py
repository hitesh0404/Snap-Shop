from django import template

register = template.Library()

@register.filter("total")
def total(value,value2):
    return value * value2
