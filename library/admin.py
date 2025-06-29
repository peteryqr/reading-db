from django.contrib import admin
from .models import LibraryUser, Book

@admin.register(LibraryUser)
class LibraryUserAdmin(admin.ModelAdmin):
    list_display = ('name', 'age')
    filter_horizontal = ('liked_books',)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
