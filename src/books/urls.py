# -*- coding: utf-8 -*-

from django.conf.urls import patterns
from books import views
from django.views.generic import TemplateView
from django.conf.urls import patterns, url
from books.views import PublisherList,PublisherBookList,BookList,AuthorDetailView,MyView
import django_databrowse

urlpatterns = patterns('',
    (r'^django_databrowse/(.*)', django_databrowse.site.root),
    (r'^filters_test$', views.filters_test),
    (r'^tags_test$', views.tags_test),
    (r'^about/', MyView.as_view()),
    url(r'^publishers/$', PublisherList.as_view()),
    (r'^books/$', BookList.as_view()),
    (r'^books/([\w-]+)/$', PublisherBookList.as_view()),
    url(r'^authors/(?P<pk>\d+)/$', AuthorDetailView.as_view(), name='author-detail'),
)


from books.models import Publisher, Author, Book
django_databrowse.site.register(Publisher)
django_databrowse.site.register(Author)
django_databrowse.site.register(Book)