from django.contrib import admin

# Register your models here.
from .models import Author, Genre, Book, BookInstance, Language

""" Minimal registration of Models.
# imports the models and then calls admin.site.register to register
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(BookInstance)
admin.site.register(Genre)
admin.site.register(Language)
"""
# Improve classes except genre & language, because they only have one field each, no benefits and no need
admin.site.register(Genre)
admin.site.register(Language)

class BooksInline(admin.TabularInline):
    """Defines format of inline book insertion (used in AuthorAdmin)"""
    model = Book

# Register the Admin classes using the decorator, @register = admin.site.register()
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    # organize the layout, date_of_birth & date_of_death layout change from vertically to horizontally
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    inlines = [BooksInline]

# Inline editing: edit BookInstance at Book
class BooksInstanceInline(admin.TabularInline):
    model = BookInstance

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # genre-book = ManyToMany relationship, display genre directly will cause large database cost
    # Instead we'll define a display_genre function to get the information as a string
    list_display = ('title', 'author', 'display_genre')
    inlines = [BooksInstanceInline]

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    """
    - fields to be displayed in list view (list_display)
    - filters that will be displayed in sidebar (list_filter)
    - grouping of fields into sections (fieldsets)
    """
    list_display = ('book', 'status', 'borrower', 'due_back')
    list_filter = ('status', 'due_back')

    # title (or None, if you don't want a title) and an associated tuple of fields in a dictionary
    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back', 'borrower')
        }),
    )