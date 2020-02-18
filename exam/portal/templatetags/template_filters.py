from django import template

register = template.Library()

@register.filter
def compute(value): 
  return round(eval(value),2)
