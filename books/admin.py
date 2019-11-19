from django.contrib import admin
from .models import Book, Publisher, Author, Store
# Register your models here.

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'get_authors']
    search_fields = ['authors__first_name']

    def get_authors(self, obj):
        return " | ".join([str(author) for author in obj.authors.all()])

@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    pass

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass

@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    pass