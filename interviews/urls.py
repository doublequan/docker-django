from django.conf.urls import url
from . import views

app_name = 'interviews'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^newest/$', views.newest, name='newest'),
]