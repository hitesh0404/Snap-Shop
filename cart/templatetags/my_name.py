from django import template

register = template.Library()

@register.filter("total")
def total(value,value2):

    return value * value2



@register.filter('myfilter')
def my_filter(value):
    return '<h1>'+value + '</h1>'
# register.filter('t',total)

# register.filter('my_filter',total)


@register.simple_tag
def mytag(user,a,b,):
     return user+a+b