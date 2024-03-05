from django.contrib import admin
from . import models
# Register your models here.
@admin.register(models.Author)
class AuthorAdmin(admin.ModelAdmin):
    model=models.Author

@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):
    model=models.Book

@admin.register(models.BookInstance)
class BookInstance(admin.ModelAdmin):
    model=models.BookInstance

@admin.register(models.Genre)
class GenreAdmin(admin.ModelAdmin):
    model=models.Genre

