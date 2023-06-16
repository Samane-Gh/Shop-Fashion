# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager


class Category(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self) :
        return self.name


class Post(models.Model):
    image =models.ImageField(upload_to='blog/',default='blog/defult.jpg')
    auther =models.ForeignKey(User, on_delete=models.SET_NULL,null=True)
    title = models.CharField(max_length=350)
    content = models.TextField() 
    tags = TaggableManager()
    Category =models.ManyToManyField(Category)
    counted_views = models.IntegerField()
    status = models.BooleanField(default=False)
    login_required = models.BooleanField(default=False)
    creted_date = models.DateTimeField(auto_now=True)
    updated_date = models.DateTimeField(auto_now=True) #2023-05-01 07:04:11.160718
    published_date = models.DateTimeField(null=True)

    def __str__(self):
         return self.title
     
    def snippets(self):
        
        l =self.content.split()[:3]
        listToStr = ' '.join(map(str, l))
        return listToStr +' ...'
    
    def get_absolute_url(self):
        return reverse('blog:single',kwargs={'pid':self.id})
    
class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    massage = models.TextField()
    created_date = models.DateTimeField(auto_now=True) 
    updated_date = models.DateTimeField(auto_now=True)
    approved = models.BooleanField(default=False)
    
    class Meta:
        ordering = ('created_date',)
    def __str__(self):
        return self.name