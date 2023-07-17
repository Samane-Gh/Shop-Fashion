from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager
from django.db import models
from django.utils import timezone
import datetime



class Category(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self) :
        return self.name


class Product(models.Model):
    image =models.ImageField(upload_to='shop/',default='shop/defult.jpg')
    title = models.CharField(max_length=350)
    price = models.IntegerField()
    content = models.TextField() 
    color = models.CharField(max_length=255)
    size = models.CharField(max_length=255)
    substance = models.CharField(max_length=255)
    Category =models.ManyToManyField(Category)
    counted_views = models.IntegerField()
    status = models.BooleanField(default=False)
    login_required = models.BooleanField(default=False)
    published_date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
         return self.title
     
    def snippets(self):
        
        l =self.content.split()[:3]
        listToStr = ' '.join(map(str, l))
        return listToStr +' ...'
    
    def get_absolute_url(self):
        return reverse('shop:details',kwargs={'pid':self.id})
    
    @staticmethod
    def get_products_by_id(pid):
        return Product.objects.filter(id__in=pid)
  
    @staticmethod
    def get_all_products():
        return Product.objects.all()
  
class Order(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    address = models.CharField(max_length=50, default='', blank=True)
    phone = models.CharField(max_length=50, default='', blank=True)
    date = models.DateField(default=timezone.now)
    status = models.BooleanField(default=False)
  
    def placeOrder(self):
        self.save()
  
    @staticmethod
    def get_orders_by_customer(pid):
        return Order.objects.filter(customer=pid).order_by('-date')
    
class Newsletter(models.Model):
    email = models.EmailField()
     
    def __str__(self):
        return self.email
    
class shopComment(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    massage = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved = models.BooleanField(default=True)
    
    class Meta:
        ordering = ('created_date',)
    def __str__(self):
        return self.name
    
class Calender(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateTimeField(default=timezone.now)
    date_time = models.DateTimeField(default=timezone.now)
    
    class Meta:
        pass
    def __str__(self):
        return self.name
    
  
    
# class Cart(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     created_at = models.DateTimeField(default= timezone.now)
#     product = models.ForeignKey(Product, on_delete=models.CASCADE,null=True)
#     quantity = models.IntegerField(default=1)
#     price_t = models.FloatField(null=True)
    
#     tax = 19.25
    
#     def price_total(self):
#         return self.price_t * (1 + 19.25 /100.0) 
    
#     def __str__(self):
#         return self.product.name + " - " + self.product


# class ProductOrder(models.Model):
#     # cart = models.ForeignKey(Cart, null=True, blank=True,on_delete=models.CASCADE)
#     user = models.ForeignKey(User, null=True,on_delete=models.CASCADE)
#     product = models.ForeignKey(Product,on_delete=models.CASCADE)
#     quantity = models.IntegerField(default=0)
#     order_date = models.DateTimeField(default=timezone.now)
#     updated_date = models.DateTimeField(default=timezone.now)
#     active = models.BooleanField(default=True)
#     unit_price = models.IntegerField(default=0)

#     def __str__(self):
#         return 'Order #' + (self.id) + ' of ' + self.product.title

# class Cart(models.Model):
#     user = models.ForeignKey(User,on_delete=models.CASCADE)
#     active = models.BooleanField(default=True,null=True)
#     order_date = models.DateField(default=timezone.now)
#     price_total = models.IntegerField(default=0)

#     def __str__(self): 
#             return "%s" % (self.user)

    # def cart_add(self, pid):
    #     product = Product.objects.get(id=pid)
    #     try:
    #         preexisting_order = ProductOrder.objects.get(product=product, cart=self)
    #         preexisting_order.quantity += 1
    #         preexisting_order.save()
    #     except ProductOrder.DoesNotExist:
    #         new_order = ProductOrder.objects.create(
    #             product=product,
    #             cart=self,
    #             quantity=1
    #             )
    #         new_order.save()

    #         def __str__(self):
    #             return "%s" % (self.pid)