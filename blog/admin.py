from django.contrib import admin
from .models import Post, Comment, Category

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'updated_at')
    list_filter = ('categories', 'created_at')
    search_fields = ('title', 'content')

admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
admin.site.register(Category)

