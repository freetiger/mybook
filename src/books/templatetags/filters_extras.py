# -*- coding: utf-8 -*-
'''
Created on 2014年11月18日

@author: heyuxing
'''
from django import template

register = template.Library()

@register.filter(name='cut2')
def cut2(value, arg):
    return value.replace(arg, '')+str("hyx")

@register.filter
def lower(value):
    return value.lower()

# register.filter('cut2', cut2)
register.filter('lower', lower)