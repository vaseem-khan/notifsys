from django.conf.urls import patterns, url
from listing import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^product/(?P<product_name_url>\w+)/$', views.products_page, name='products_page'),)