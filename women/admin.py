from django.contrib import admin
from .models import *


@admin.register(Women)
class WomenAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'is_published', 'time_create', 'time_update']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', ]
