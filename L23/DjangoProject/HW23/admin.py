from django.contrib import admin
from .models import *
from django.db.models import Avg
# Register your models here.

class GamesDevAdmin(admin.ModelAdmin):
    list_display = ('nameDev',)
    list_display_links = ('nameDev',)

class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'is_active','game_amount', 'average_cost',)
    list_display_links = ('title', 'description', 'is_active',)
    list_filter = ('title', 'description', 'is_active','game_amount',)
    
    @admin.display(description="average cost (средняя цена)")
    def average_cost(self, obj):
        return round(Games.objects.filter(category = obj).aggregate(Avg('price'))['price__avg'],2)



class GamesAdmin(admin.ModelAdmin):
    list_display = ('name', 'gameDev', 'release_date', 'category', 'is_active', 'status', 'slug', 'upd_date', 'img_preview',)
    list_display_links = ('name',)
    search_fields = ('name', 'gameDev', 'release_date', 'category', 'is_active', 'status',)
    fields = ('name', 'gameDev', 'release_date', 'category', 'price', 'description', 'is_active', 'status', 'game_image', 'slug',)
    
    @admin.display(description='game image')
    def img_preview(self, obj):
        from django.utils.html import mark_safe
        return mark_safe(f'<img src = "{obj.game_image.url}" height="75px"/>')

class StatusAdmin(admin.ModelAdmin):
    list_display = ('status_name',)
    search_fields = ('status_name',)

admin.site.register(GamesDev, GamesDevAdmin)
admin.site.register(Categories, CategoriesAdmin)
admin.site.register(Games, GamesAdmin)
admin.site.register(Status, StatusAdmin)