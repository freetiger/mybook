# -*- coding: utf-8 -*-
'''
Created on 2014年11月6日

@author: heyuxing
'''
from django.contrib import admin
from books.models import Publisher, Author, Book
 
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
    search_fields = ('first_name', 'last_name')
    
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'publisher', 'publication_date')
    list_filter = ('publication_date',)
    date_hierarchy = 'publication_date'
    ordering = ('-publication_date',)
    #fields = ('title', 'authors', 'publisher', 'publication_date')
    #filter_horizontal = ('authors',)    #我们强烈建议针对那些拥有十个以上选项的`` 多对多字段`` 使用filter_horizontal。
    #raw_id_fields = ('publisher',)
 
admin.site.register(Publisher)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)

