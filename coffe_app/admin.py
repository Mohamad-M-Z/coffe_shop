from django.contrib import admin
from .models import Menu, Category, Contact, Newsletter

# Register your models here.

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'status', 'created_date', 'published_date')
    list_filter = ('name', 'price')
    search_fields = ('name', 'content')


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    list_display = ('name', 'email', 'created_date')
    list_filter = ('email',)
    search_fields = ('name', 'message')


admin.site.register(Newsletter)
admin.site.register(Category)
