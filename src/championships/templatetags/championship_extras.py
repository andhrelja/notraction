from django import template

register = template.Library()

@register.filter
def results(subcategory, championship):
    return subcategory.results(championship)

@register.filter
def top_results(subcategory, championship):
    return subcategory.top_results(championship)

@register.filter
def driver_results(subcategory, driver):
    return subcategory.driver_results(driver)


@register.filter
def driver_championship_results(subcategory, championship):
    return subcategory.filter(championship=championship)

@register.filter
def driver_categories(championship, driver):
    return championship.championship_type.category_set.filter(driver=driver)
