
from django import urls
from django.urls import path
from shop.views import *
# from shop.feeds import LatestEntriesFeed

app_name ='shop'

urlpatterns = [
    
    path('',shop_view,name='index' ),
    path('details/<int:pid>',shop_details,name='details'),
    path('category/<str:cat_name>',shop_category,name='category'),
    path('category/<str:cat_name>',shop_view,name='category'),
    path('details',shop_details,name='details'),
    path('search/',shop_search,name='search'),
    path('add/<int:pid>/',cart_add, name='cart_add'),
    path('cart_detail/',cart_detail, name='cart_detail'),
	path('remove/<int:pid>/', cart_remove, name='cart_remove'),
      
] 