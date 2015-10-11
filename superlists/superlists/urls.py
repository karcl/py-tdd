from django.conf.urls import patterns, include, url
from django.contrib import admin
from lists import views

urlpatterns = patterns('',
    url(r'^$', views.home_page, name='home'),
    url(r'^lists/new$', views.new_list, name='new_list'),
    url(r'^lists/the-only-list-in-the-world/$', views.view_list, name='view_list'),


    #url(r'^admin/', include(admin.site.urls)),
)
