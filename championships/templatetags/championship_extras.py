from django import template

register = template.Library()

@register.filter
def results(subcategory, championship):
    return subcategory.results(championship)

@register.filter
def top_results(subcategory, championship):
    return subcategory.top_results(championship)