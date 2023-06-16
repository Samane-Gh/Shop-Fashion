from django.contrib import admin
from blog.models import Post,Category,Comment
from django_summernote.admin import SummernoteModelAdmin

class PostAdmin(SummernoteModelAdmin):
    #date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display =('title','auther', 'counted_views', 'status','login_required','published_date', )
    list_filter = ('status','auther', )
    search_fields = ['title','content']
    summernote_fields = ('content',)

class CommentAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    list_display =('name','post', 'approved','created_date', )
    list_filter = ('post','approved', )
    search_fields = ['name','post']

admin.site.register(Comment,CommentAdmin)
admin.site.register(Category)
admin.site.register(Post,PostAdmin)



# Register your models here.
