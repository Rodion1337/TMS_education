from django.contrib import admin
from .models import *
# Register your models here.

class GamesDevAdmin(admin.ModelAdmin):
    list_display = ('nameDev',)
    list_display_links = ('nameDev',)

class categoriesAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'is_active',)
    list_display_links = ('title', 'description', 'is_active',)
    list_filter = ('title', 'description', 'is_active',)

class gamesAdmin(admin.ModelAdmin):
    list_display = ('name', 'gameDev', 'release_date', 'category', 'is_active_game',)
    list_display_links = ('name',)
    search_fields = ('name', 'gameDev', 'release_date', 'category', 'is_active_game',)

admin.site.register(GamesDev, GamesDevAdmin)
admin.site.register(categories, categoriesAdmin)
admin.site.register(games, gamesAdmin)