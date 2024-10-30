from django.contrib import admin
from .models import Menu, Category

# Register your models here.

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'status', 'created_date', 'published_date')
    list_filter = ('name', 'price')
    search_fields = ('name', 'content')


admin.site.register(Category)