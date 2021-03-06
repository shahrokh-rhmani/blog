from django.contrib import admin
from .models import Post, Category


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status',)
    prepopulated_fields = {'slug':('title',)}



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass
