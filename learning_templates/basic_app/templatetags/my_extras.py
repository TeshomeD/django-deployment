from django import template

register = template.Library()

@register.filter(name='cutarg')
def cut_arg(value, arg):
    '''
        This function cuts out all values of the arg from string
    '''
    return value.replace(arg, '')

#register.filter('cutarg',cut_arg)