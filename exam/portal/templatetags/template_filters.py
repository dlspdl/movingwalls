from django import template

register = template.Library()

@register.filter
def compute(value): 
  return round(eval(value),2)

@register.filter 
def has_group(user, group_name):
    return user.groups.filter(name=group_name).exists() 
