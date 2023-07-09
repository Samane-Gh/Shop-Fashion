from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render,get_object_or_404
from shop.models import Product,Comment
from shop.models import Category
from django.utils import timezone
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from blog.forms import CommentForm
from django.urls import reverse
from blog.forms import NewsletterForm
from jalali_date import datetime2jalali, date2jalali
from django.template.defaultfilters import date


# Create your views here.
def shop_view(request,**kwargs): 
    products = Product.objects.filter(status=1).order_by('title')
    #products = Product.objects.filter(status=1).order_by('published_date')
    # if kwargs.get('cat_name') != None:
    #     products = products.filter(Category__name=kwargs['cat_name'])
    # if kwargs.get('color_name') != None:
    #     products = products.filter(color__username =kwargs['color_name'])  
    #     if kwargs.get('size_name') != None: 
    #         products = products.filter(size__name__in =kwargs['size_name'])
    products = Paginator(products,6) 
    try: 
        page_number = request.GET.get('page')
        products = products.get_page(page_number)
    except PageNotAnInteger:
        products = products.get_page(1)
    except EmptyPage:
        products = products.get_page(1)
    contex = {'products': products}
    return render(request,'shop/shop-home.html',contex)


def shop_details(request,pid=None):    
    product = get_object_or_404(Product, id = pid)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'your comment submited successfully')
        else:
           messages.add_message(request,messages.ERROR,'your comment did not submited successfully')        
    product = Product.objects.get(id =pid)
    product.counted_views +=1
    product.save()
    next_product = Product.objects.filter(published_date__gt=product.published_date).order_by('published_date').first()
    prev_product =Product.objects.filter(published_date__lt=product.published_date).order_by('published_date').last()
    if not product.login_required:
        comments = Comment.objects.filter(product=product.id , approved=True)
        form = CommentForm()
        contex = {'product': product,'next_product': next_product,'prev_product': prev_product,'comments': comments,'form': form}
        return render(request,'shop/details.html',contex)
    elif product.login_required:
        if request.user.is_authenticated:
            comments = Comment.objects.filter(product=product.id , approved=True)
            form = CommentForm()
            contex = {'product': product,'next_product': next_product,'prev_product': prev_product,'comments': comments,'form': form}
            return render(request,'shop/details.html',contex)
        else:
            return HttpResponseRedirect(reverse('accounts:login')) 
    else:
        return HttpResponseRedirect(reverse('accounts:login'))   
    
def newsletter_view(request):
    if request.method == 'POST':
        form =NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')      
        
def shop_category(request,cat_name):
    products = Product.objects.filter(status=1)
    products = products.filter(Category__name=cat_name)
    contex ={'products': products}
    return render(request,'shop/shop-home.html',contex)

def shop_search(request):
    products = Product.objects.filter(status=1)
    if request.method == 'GET' :
        if request.GET.get('s'):
           products = products.filter(content__contains=request.GET.get('s')) 
        #print(request.GET.get('s'))   
    contex = {'products': products}
    return render(request,'shop/shop-home.html',contex)  


def my_view(request):
	jalali_join1 = (datetime2jalali(request.user.date_joined)).strftime('%B')

    

