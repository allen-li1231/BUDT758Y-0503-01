from django import template

register = template.Library()


@register.filter
def replace_space_bl(string):
    return string.replace(' ', '_')