from django.contrib import admin
from .models import *


class BdAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'price', 'publisher')
    list_display_links = ('title', 'content')
    search_fields = ('title', 'content',)

class userAdmin(admin.ModelAdmin):
    list_display = ('login', 'firstname', 'lastname', 'email', 'password')
    list_display_links = ('login', 'email')
    search_fields = ('login', 'email')

class categoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    list_display_links = ('title', 'description')

class postAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'published', 'author')
    list_display_links = ('title', 'content', 'published', 'author')

admin.site.register(Bd, BdAdmin)
admin.site.register(user, userAdmin)
admin.site.register(category, categoryAdmin)
admin.site.register(post, postAdmin)

# Register your models here.
