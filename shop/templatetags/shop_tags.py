from django import template
from shop.models import Product,shopComment ,Order
from shop.models import Category
register = template.Library()

@register.simple_tag(name='totalposts')
def function():
    products = Product.objects.filter(status=1)
    return products

@register.simple_tag(name='shopcomments_count')
def function(pid):
    return shopComment.objects.filter(product=pid,approved=True).count()

@register.simple_tag(name='order_count')
def orderCount(user_id):
    return Order.objects.filter(user=user_id,status=True).count()
    
@register.inclusion_tag('shop/shop-popular.html')
def popularproducts(arg=4):
    products = Product.objects.order_by('-counted_views')[:arg]
    return {'products': products}

@register.inclusion_tag('shop/shop-categories.html')
def productcategories():
    products = Product.objects.filter(status=1)
    Categories = Category.objects.all()
    cat_dict = {}
    for name in Categories:
        cat_dict[name]=products.filter(Category=name).count()    
    return {'categories': cat_dict}

@register.inclusion_tag('shop/shop-arrivals.html')
def latest_products(arg=3):
    products = Product.objects.filter(status=1).order_by('-published_date')[:arg]
    return {'products': products }

@register.inclusion_tag('shop/index-shop-arrivals.html')
def new_products(arg=4):
    products = Product.objects.filter(status=1).order_by('-published_date')[:arg]
    return {'products': products }
