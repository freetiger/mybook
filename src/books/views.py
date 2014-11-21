# -*- coding: utf-8 -*-
'''
Created on 2014年10月31日

@author: heyuxing
'''
import datetime

from django.shortcuts import render_to_response

from django.views.generic import ListView,View
from books.models import Publisher,Book
from django.shortcuts import get_object_or_404
from django.http import HttpResponse

def filters_test(request):
    current_date = datetime.datetime.now()
    return render_to_response('filters_test.html', {'current_date': str(current_date)})
    
def tags_test(request):
    current_date = datetime.datetime.now()
    return render_to_response('tags_test.html', {'current_date': str(current_date)})
    
class PublisherList(ListView):
    model = Publisher
    
class BookList(ListView):
    queryset = Book.objects.order_by('-publication_date')
    context_object_name = 'book_list'

class PublisherBookList(ListView):

    template_name = 'books/books_by_publisher.html'

    def get_queryset(self):
        self.publisher = get_object_or_404(Publisher, name=self.args[0])
        return Book.objects.filter(publisher=self.publisher)
    
from django.views.generic import DetailView
from django.utils import timezone
from books.models import Author
class AuthorDetailView(DetailView):

    queryset = Author.objects.all()
    #如果想要在对数据库进行访问之前（或后）实现一些额外的操作，那么可以通过封装 类视图的 get_object() 方法来实现。
    def get_object(self):
        # Call the superclass
        object = super(AuthorDetailView, self).get_object()
        # Record the last accessed date
        object.last_accessed = timezone.now()
        object.save()
        # Return the object
        return object
    
class MyView(View):
    def get(self, request):
        # <view logic>
        return HttpResponse('result')  
    
    