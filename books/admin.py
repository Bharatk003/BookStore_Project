 
# books/admin.py
from django.contrib import admin
from .models import book, Review
class ReviewInline(admin.TabularInline):
    model = Review


class BookAdmin(admin.ModelAdmin):
    inlines = [
    ReviewInline,
                ]
    list_display = ("title", "author", "price",)


admin.site.register(book, BookAdmin)