from django.contrib import admin
from .models import Post
from django.contrib.auth.models import Group
from django.contrib.auth.models import User

class PostAdmin(admin.ModelAdmin):
    exclude = ('slug',)

admin.site.register(Post, PostAdmin)
admin.site.unregister(Group)
admin.site.unregister(User)