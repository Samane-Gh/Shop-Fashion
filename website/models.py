#database  is in this file
from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    subject = models.CharField(blank=True ,null=True , max_length=255) 
    massage = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['created_date']
    def __str__(self):
        return self.name  
 
class Newsletter(models.Model):
    email = models.EmailField()
     
    def __str__(self):
        return self.email
   
# Create your models here.
