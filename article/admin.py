from django.contrib import admin

from .models import (
    Category,
    Tag,
    Author,
    Article,
    Comments,
)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    search_fields = ('title',)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    search_fields = ('title',)


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'title', 'created_date')
    readonly_fields = ('slug', 'modified_date', 'created_date', 'slug')
    search_fields = ('title',)
    list_filter = ('category', 'tags')
    date_hierarchy = 'created_date'
    filter_horizontal = ('tags',)
    save_on_top = True


@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    search_fields = ('name', 'article__title', )
    readonly_fields = ('created_date',)
    list_display = ('id', 'article', 'name', 'email', 'top_level_comment_id', 'get_image', 'created_date',)
    autocomplete_fields = ('article',)


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name', )


