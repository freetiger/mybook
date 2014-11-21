# -*- coding: utf-8 -*-
'''
Created on 2014年11月18日

@author: heyuxing
'''
from django import template

register = template.Library()

#自定义标签
@register.tag(name="current_time")
def do_current_time(parser, token):
    try:
        # split_contents() knows not to split quoted strings.
        tag_name, format_string = token.split_contents()
        print token.split_contents()[0]
        print tag_name
    except ValueError:
        msg = '%r tag requires a single argument' % token.split_contents()[0]
        raise template.TemplateSyntaxError(msg)
    return CurrentTimeNode(format_string[1:-1])

import datetime
class CurrentTimeNode(template.Node):
    def __init__(self, format_string):
        self.format_string = str(format_string)

    def render(self, context):
        now = datetime.datetime.now()
        return now.strftime(self.format_string)

#在上下文中设置变量
@register.tag(name="current_time2")
def do_current_time2(parser, token):
    try:
        # split_contents() knows not to split quoted strings.
        tag_name, format_string = token.split_contents()
        print token.split_contents()[0]
        print tag_name
    except ValueError:
        msg = '%r tag requires a single argument' % token.split_contents()[0]
        raise template.TemplateSyntaxError(msg)
    return CurrentTimeNode2(format_string[1:-1])
   
class CurrentTimeNode2(template.Node):
    def __init__(self, format_string):
        self.format_string = str(format_string)

    def render(self, context):
        now = datetime.datetime.now()
        context['current_time2'] = now.strftime(self.format_string)
        return ''
    
register.tag('current_time', do_current_time)