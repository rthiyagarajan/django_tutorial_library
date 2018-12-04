from django.contrib import admin

# Register your models here.
from catalog.models import Author, Genre, Book, BookInstance, Language

# admin.site.register(Book)
# admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Language)
# admin.site.register(BookInstance)



class BookInstanceInline(admin.StackedInline):
	model = Book
	extra = 0

# define ModelAdmin class
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')] # in detail view
    inlines = [BookInstanceInline]

admin.site.register(Author, AuthorAdmin)





# This will allow the BookInstances to be visible and editable  in the Book detailed view
class BooksInstanceInline(admin.TabularInline):
    model = BookInstance
    extra = 0 # don't show extra book instances

# Register the Admin classes for Book using the decorator - same as using class for AuthorAdmin above
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BooksInstanceInline]



# Register the Admin classes for BookInstance using the decorator
@admin.register(BookInstance) 
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'borrower', 'due_back','id')
    list_filter = ('status', 'due_back') # filters on the right side of book instance - awesome
    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back', 'borrower')
        }),
    )