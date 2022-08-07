from django.contrib import admin
from .models import News, NewsType


class NewsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']


class NewsTypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'code']


admin.site.register(News, NewsAdmin)
admin.site.register(NewsType, NewsTypeAdmin)
