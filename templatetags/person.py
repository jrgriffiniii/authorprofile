from django import template

register = template.Library()

@register.filter(name='deepestPath')
def deepestPath(value):

    return value[-1].edges
