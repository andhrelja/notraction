from django import template

register = template.Library()

@register.filter
def results(subcategory, championship):
    return subcategory.results(championship)