from django.contrib import admin
from blog.models import Post, blogComment
# Register your models here.

admin.site.register(blogComment)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    class Media:
        js = ('tiny.js',)
