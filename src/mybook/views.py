# -*- coding: utf-8 -*-
'''
Created on 2014年10月31日

@author: heyuxing
'''
from django.http import HttpResponse,Http404
from django.shortcuts import render_to_response
import datetime

from books.models import Book

def index(request):
    return HttpResponse("我自己写的index页啊啊啊")

def hello(request):
    return HttpResponse("Hello world")

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    #assert False
    html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    return HttpResponse(html)

def current_datetime_2(request):
    current_date = datetime.datetime.now()
    return render_to_response('dateapp/current_datetime2.html', {'current_date': current_date})
    #return render_to_response('dateapp/current_datetime2.html', locals())
    
def current_datetime_3(request):
    current_date = datetime.datetime.now()
    return render_to_response('dateapp/current_datetime3.html', {'current_date': current_date})
    
def display_meta(request):
    values = request.META.items()
    values.sort()
    html = []
    html.append('<tr><td>%s</td><td>%s</td></tr>' % ('path', request.path))
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))

def search(request):
    errors = []
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append('Enter a search term.')
        elif len(q) > 20:
            errors.append('Please enter at most 20 characters.')
        else:
            books = Book.objects.filter(title__icontains=q)
            return render_to_response('dateapp/search_results.html',
                {'books': books, 'query': q})
    return render_to_response('dateapp/search_form.html',
        {'errors': errors })
    
    
    

