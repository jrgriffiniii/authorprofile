from django import template

register = template.Library()

@register.filter(name='deepestPath')
def deepestPath(value):

    return value[-1].edges

@register.filter(name='authorName')
def authorName(value):

    if value.ids:

        return value.ids[0].value
    else:

        return value.name
