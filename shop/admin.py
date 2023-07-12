from django.contrib import admin
from shop.models import Product,Category,shopComment
from django_summernote.admin import SummernoteModelAdmin

class ProductAdmin(SummernoteModelAdmin):
    #date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display =('title','price', 'counted_views', 'status','login_required','published_date', )
    list_filter = ('status', )
    search_fields = ['title','content','color','price']
    summernote_fields = ('content',)

class CommentAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    list_display =('name','subject', 'email', )
    list_filter = ('name','approved', )
    search_fields = ['name','subject','massage']

admin.site.register(shopComment,CommentAdmin)
admin.site.register(Category)
admin.site.register(Product,ProductAdmin)



# Register your models here.

