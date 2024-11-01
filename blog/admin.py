from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    exclude = ('slug',)  # Exclude slug from admin interface

admin.site.register(Post, PostAdmin)
