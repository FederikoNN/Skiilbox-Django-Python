from django.contrib import admin
from .models import Author, Book


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name']


admin.site.register(Author, AuthorAdmin)
admin.site.register(Book)
