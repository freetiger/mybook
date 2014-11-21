from django.conf.urls import patterns, include, url
from django.contrib import admin
from mybook.views import hello,index,current_datetime,hours_ahead,current_datetime_2,current_datetime_3, display_meta
from mybook import views
from contact.views import contact

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mybook.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    ('^$', index),
    ('^hello/$', hello),
    ('^time/$', current_datetime),
    ('^another-time-page/$', current_datetime),
    (r'^time/plus/(\d{1,2})/$', hours_ahead),
    (r'^time2/$', current_datetime_2),
    (r'^time3/$', current_datetime_3),
    (r'^display_meta/$', display_meta),
    (r'^search/$', views.search),
    (r'^contact/$', contact),
    
     url(r'^books/', include('books.urls', namespace="books")),
)
