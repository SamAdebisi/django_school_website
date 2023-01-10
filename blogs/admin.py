from django.contrib import admin

from .models import Blog, Comment


class CommentInline(admin.TabularInline):
    model = Comment


class BlogAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline,
    ]
    list_display = ('title', 'author', 'body', 'date')


admin.site.register(Blog, BlogAdmin)
