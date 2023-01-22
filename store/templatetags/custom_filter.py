from django import template

register = template.Library()

@register.filter(name='currancy')
def currency(number):
            return "Rs "+str(number)


