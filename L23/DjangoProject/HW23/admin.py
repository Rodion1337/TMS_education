from django.contrib import admin
from .models import *
# Register your models here.

class GamesDevAdmin(admin.ModelAdmin):
    list_display = ('nameDev',)
    list_display_links = ('nameDev',)

class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'is_active','game_amount',)
    list_display_links = ('title', 'description', 'is_active',)
    list_filter = ('title', 'description', 'is_active','game_amount',)

class GamesAdmin(admin.ModelAdmin):
    list_display = ('name', 'gameDev', 'release_date', 'category', 'is_active', 'status',)
    list_display_links = ('name',)
    search_fields = ('name', 'gameDev', 'release_date', 'category', 'is_active', 'status',)
    fields = ('name', 'gameDev', 'release_date', 'category', 'price', 'description', 'is_active', 'status', 'game_image',)

class StatusAdmin(admin.ModelAdmin):
    list_display = ('status_name',)
    search_fields = ('status_name',)

admin.site.register(GamesDev, GamesDevAdmin)
admin.site.register(Categories, CategoriesAdmin)
admin.site.register(Games, GamesAdmin)
admin.site.register(Status, StatusAdmin)