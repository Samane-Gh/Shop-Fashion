
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
    # path('cart/',cart_view,name='cart'),
    path('add/<int:id>/',cart_add, name='cart_add'),
    path('item_clear/<int:id>/', item_clear, name='item_clear'),
    path('item_increment/<int:id>/',item_increment, name='item_increment'),
    path('item_decrement/<int:id>/',item_decrement, name='item_decrement'),
    path('cart_clear/',cart_clear, name='cart_clear'),
    path('cart_detail/',cart_detail,name='cart_detail'),
    
] 