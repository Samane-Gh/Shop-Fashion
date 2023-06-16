from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render,get_object_or_404
from blog.models import Post,Comment
from blog.models import Category
from django.utils import timezone
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from blog.forms import CommentForm
from django.urls import reverse

# Create your views here.
def blog_view(request,**kwargs): 
    #posts = Post.objects.filter(status=1).order_by('title')
    posts = Post.objects.filter(status=1).order_by('published_date')
    if kwargs.get('cat_name') != None:
        posts = posts.filter(Category__name=kwargs['cat_name'])
    if kwargs.get('ather_name') != None:
        posts = posts.filter(auther__username =kwargs['ather_name'])  
        if kwargs.get('tag_name') != None: 
            posts = posts.filter(tag__name__in =kwargs['tag_name'])
    posts = Paginator(posts,3) 
    try: 
        page_number = request.GET.get('page')
        posts = posts.get_page(page_number)
    except PageNotAnInteger:
        posts = posts.get_page(1)
    except EmptyPage:
        posts = posts.get_page(1)
    contex = {'posts': posts}
    return render(request,'blog/blog-home.html',contex)


def blog_single(request,pid=None):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'your comment submited successfully')
        else:
           messages.add_message(request,messages.ERROR,'yourc comment did not submited successfully') 
    # else:      
    #     if pid is None:
    #         contex = {'post': {}}
    #         return render(request,'blog/blog-single.html',contex)        
    post = Post.objects.get(id =pid)
    post.counted_views +=1
    next_post = Post.objects.filter(published_date__gt=post.published_date).order_by('published_date').first()
    prev_post =Post.objects.filter(published_date__lt=post.published_date).order_by('published_date').last()
    if not post.login_required:
        comments = Comment.objects.filter(post = post.id,approved=True)
        form = CommentForm()
        contex = {'post': post,'next_post': next_post,'prev_post': prev_post,'comments': comments,'form': form}
        return render(request,'blog/blog-single.html',contex)
    else:
        return HttpResponseRedirect(reverse('accounts:login'))
    
        
def blog_category(request,cat_name):
    posts = Post.objects.filter(status=1)
    posts = posts.filter(Category__name=cat_name)
    contex ={'posts': posts}
    return render(request,'blog/blog-home.html',contex)

def blog_search(request):
    posts = Post.objects.filter(status=1)
    if request.method == 'GET' :
        if request.GET.get('s'):
           posts = posts.filter(content__contains=request.GET.get('s')) 
        #print(request.GET.get('s'))   
    contex = {'posts': posts}
    return render(request,'blog/blog-home.html',contex)    



    

