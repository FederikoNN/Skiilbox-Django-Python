from django.contrib import admin
from .models import News, Comment, Tag


class CommentInLine(admin.TabularInline):
    model = Comment
    extra = 0


class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'date_create', 'date_edit', 'activity',
                    'is_active']
    list_editable = ['is_active']
    list_filter = ['is_active']
    inlines = [CommentInLine]
    actions = ['mark_is_active', 'mark_is_inactive']

    def mark_is_active(self, request, queryset):
        queryset.update(is_active=True)

    def mark_is_inactive(self, request, queryset):
        queryset.update(is_active=False)

    mark_is_active.short_description = 'Опубликовать'
    mark_is_inactive.short_description = 'Снять с публикации'


class CommentAdmin(admin.ModelAdmin):
    list_display = ['user_name', 'description_view', 'display_news_comment']
    list_display_links = ['description_view']
    list_filter = ['user_name']
    actions = ['mark_is_deleted']

    def display_news_comment(self, obj):
        news = obj.news_comment
        return f'"{news.title}" от {news.date_create}. Комментариев: ' \
               f'{news.activity}'

    def description_view(self, obj):
        if len(obj.description) <= 15:
            return obj.description
        return f'{obj.description[:15]}...'

    display_news_comment.short_description = 'Новость'
    description_view.short_description = 'Комментарий'

    def mark_is_deleted(self, request, queryset):
        queryset.update(description='Удалено администратором')

    mark_is_deleted.short_description = 'Пометить как Удалено'


admin.site.register(News, NewsAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Tag)
