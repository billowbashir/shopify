from django.conf.urls import url
from . import views


urlpatterns=[
        url(r'^$',views.home,name='Home'),
        url(r'^new_shop',views.new_shop,name='new_shop'),
        url(r'^products/(?P<shop_id>\d+)/$',views.shop_products,name='products'),
        url(r'^new_product/(?P<pk>\d+)$',views.add_product,name='new_product'),
]
