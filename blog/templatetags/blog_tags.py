from django import template
from blog.models import Post,Comment
from blog.models import Category
register = template.Library()

@register.simple_tag(name='totalposts')

def function():
    posts = Post.objects.filter(status=1)
    return posts

@register.simple_tag(name='comments_count')
def function(pid):
    return Comment.objects.filter(post=pid,approved=True).count()

@register.inclusion_tag('blog/blog-popular-posts.html')
def latestposts(arg=3):
    posts = Post.objects.filter(status=1).order_by('published_date')[:arg]
    return {'posts': posts}

@register.inclusion_tag('blog/blog-post-categories.html')
def postcategories():
    posts = Post.objects.filter(status=1)
    Categories = Category.objects.all()
    cat_dict = {}
    for name in Categories:
        cat_dict[name]=posts.filter(Category=name).count()    
    return {'categories': cat_dict}

@register.inclusion_tag('blog/blog-latest-posts.html')
def latest_posts(arg=6):
    posts = Post.objects.filter(status=1).order_by('published_date')[:arg]
    return {'posts':posts}