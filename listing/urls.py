from django.conf.urls import patterns, url
from listing import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'))