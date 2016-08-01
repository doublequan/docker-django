# coding: utf-8

from django.conf.urls import url
from . import views

app_name = 'interviews'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^search$', views.search, name='search'),
    # url(r'^search-(?P<current_page_num>[0-9]+)$', views.search, name='search'),
]