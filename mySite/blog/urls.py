
from django.urls import path
from blog.views import *
from blog.feeds import LatestEntriesFeed
app_name ='blog'

urlpatterns = [
    
    #path("url addres ", "view")
    path('',blog_view,name='index' ),
    path('single/<int:pid>',blog_single,name='single'),
    #path('category/<str:cat_name>',blog_category,name='category'),
    path('category/<str:cat_name>',blog_view,name='category'),
    path('tag/<str:tag_name>',blog_view,name='tag'),
    path('auther/<str:auther_name>',blog_view,name='auther'),
    path('single',blog_single,name='single'),
    path('search/',blog_search,name='search'),
    path('rss/feed/', LatestEntriesFeed()),
    
    #path('test',test,name='test'),
   
    
    
] 