from django.contrib import admin
from .models import Post, Category

# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    list_display = ('title', 'created_date', 'published_date', 'status')
    list_filter = ('status', 'category')
    search_fields = ('title', 'content')


# admin.site.register(Post, PostAdmin)
admin.site.register(Category)
