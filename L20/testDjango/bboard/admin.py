from django.contrib import admin
from .models import *

# admin.site.register(Bd)


@admin.register(Bd)
class BdAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'price', 'publisher')
    list_display_links = ('title', 'content')
    search_fields = ('title', 'content',)
    
# admin.site.register(Bd, BdAdmin)

admin.site.register(user)
admin.site.register(category)
admin.site.register(post)