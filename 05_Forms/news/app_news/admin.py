from django.contrib import admin
from .models import News, Comment


class CommentInLine(admin.TabularInline):
    model = Comment


class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'date_create', 'date_edit', 'activity',
                    'is_active']
    list_filter = ['is_active']
    inlines = [CommentInLine]
    actions = ['mark_is_active', 'mark_is_inactive']

    def mark_is_active(self, request, queryset):
        queryset.update(is_active=True)

    def mark_is_inactive(self, request, queryset):
        queryset.update(is_active=False)

    mark_is_active.short_description = 'Перевести в статус Активно'
    mark_is_inactive.short_description = 'Перевести в статус Неактивно'


class CommentAdmin(admin.ModelAdmin):
    list_display = ['user_name', 'description', 'news_comment']
    list_filter = ['user_name']
    actions = ['mark_is_deleted']

    def mark_is_deleted(self, request, queryset):
        queryset.update(description='Удалено администратором')

    mark_is_deleted.short_description = 'Пометить как Удалено'


admin.site.register(News, NewsAdmin)
admin.site.register(Comment, CommentAdmin)
