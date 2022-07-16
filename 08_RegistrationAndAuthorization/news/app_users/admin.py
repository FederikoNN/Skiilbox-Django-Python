from django.contrib import admin
from .models import Profile


# from django.contrib.auth.admin import UserAdmin
#
# UserAdmin.fieldsets = ('Custom field set', {
#     'fields': ('phone', 'city', 'is_verified', 'published_news')}),
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'is_verified']
    list_editable = ['is_verified']
    list_filter = ['is_verified']
    actions = ['mark_is_verified', 'mark_is_not_verified']

    def mark_is_verified(self, request, queryset):
        queryset.update(is_verified=True)

    def mark_is_not_verified(self, request, queryset):
        queryset.update(is_verified=False)

    mark_is_verified.short_description = 'Верифицировать пользователя'
    mark_is_not_verified.short_description = 'Отменить верификацию'


admin.site.register(Profile, ProfileAdmin)
