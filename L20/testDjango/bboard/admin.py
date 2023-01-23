from django.contrib import admin
from .models import Bd

# admin.site.register(Bd)


@admin.register(Bd)
class BdAdmin(admin.ModelAdmin):
    pass