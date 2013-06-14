from django import template

register = template.Library()

@register.filter(name='deepestPath')
def deepestPath(paths):

    if paths:

        return paths[-1].edges

    return paths

@register.filter(name='authorName')
def authorName(value):

    if value.ids:

        return value.ids[0].value

    return value.name
