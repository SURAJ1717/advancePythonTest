from django.contrib import admin
from firstApp.models import BooksAuthor, BooksLanguage, BooksSubject, BooksFormat, BooksBookshelf, BooksBookSubjects, BooksBookLanguages, BooksBookBookshelves, BooksBookAuthors, BooksBook

# Register your models here.
admin.site.register(BooksAuthor)
admin.site.register(BooksLanguage)
admin.site.register(BooksSubject)
admin.site.register(BooksFormat)
admin.site.register(BooksBookshelf)
admin.site.register(BooksBookSubjects)
admin.site.register(BooksBookLanguages)
admin.site.register(BooksBookBookshelves)
admin.site.register(BooksBook)
admin.site.register(BooksBookAuthors)
