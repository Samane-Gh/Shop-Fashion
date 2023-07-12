
from django import urls
from django.urls import path
from shop.views import *
# from shop.feeds import LatestEntriesFeed

app_name ='blog'

urlpatterns = [
    
    path('',shop_view,name='index' ),
    path('details/<int:pid>',shop_details,name='details'),
    path('category/<str:cat_name>',shop_category,name='category'),
    path('category/<str:cat_name>',shop_view,name='category'),
    path('details',shop_details,name='details'),
    path('search/',shop_search,name='search'),
    # path('rss/feed/', LatestEntriesFeed()),
    
] 