from django import template

register = template.Library()

@register.filter
def compute(value): 
  return eval(value)
