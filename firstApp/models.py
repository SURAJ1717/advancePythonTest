from django.db import models

# Create your models here.
class BooksAuthor(models.Model):
    id = models.IntegerField(primary_key=True)
    birth_year = models.SmallIntegerField(blank=True, null=True)
    death_year = models.SmallIntegerField(blank=True, null=True)
    name = models.CharField(max_length=128)
    class Meta:
        managed = False
        db_table = 'books_author'

class BooksBookshelf(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=64)
    class Meta:
        managed = False
        db_table = 'books_bookshelf'

class BooksLanguage(models.Model):
    id = models.IntegerField(primary_key=True)
    code = models.CharField(max_length=4)
    class Meta:
        managed = False
        db_table = 'books_language'

class BooksSubject(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField()
    class Meta:
        managed = False
        db_table = 'books_subject'

class BooksBook(models.Model):
    id = models.IntegerField(primary_key=True)
    download_count = models.IntegerField(blank=True, null=True)
    gutenberg_id = models.IntegerField()
    media_type = models.CharField(max_length=16)
    title = models.TextField(blank=True, null=True)

    authors = models.ManyToManyField(
        BooksAuthor,
        through='BooksBookAuthors',
        through_fields=('book', 'author')
    )
    bookshelfs = models.ManyToManyField(
        BooksBookshelf,
        through='BooksBookBookshelves',
        through_fields=('book', 'bookshelf')
    )
    languages = models.ManyToManyField(
        BooksLanguage,
        through='BooksBookLanguages',
        through_fields=('book', 'language')
    )
    subjects = models.ManyToManyField(
        BooksSubject,
        through='BooksBookSubjects',
        through_fields=('book', 'subject')
    )
    class Meta:
        managed = False
        db_table = 'books_book'

    @property
    def formats(self):
        return self.booksformat_set.all()


class BooksFormat(models.Model):
    id = models.IntegerField(primary_key=True)
    mime_type = models.CharField(max_length=32)
    url = models.TextField()
    book = models.ForeignKey(BooksBook, on_delete=models.CASCADE)
    class Meta:
        managed = False
        db_table = 'books_format'

class BooksBookAuthors(models.Model):
    id = models.IntegerField(primary_key=True)
    book = models.ForeignKey(BooksBook, on_delete=models.CASCADE)
    author = models.ForeignKey(BooksAuthor, on_delete=models.CASCADE)
    class Meta:
        managed = False
        db_table = 'books_book_authors'

class BooksBookBookshelves(models.Model):
    id = models.IntegerField(primary_key=True)
    book = models.ForeignKey(BooksBook, on_delete=models.CASCADE)
    bookshelf = models.ForeignKey(BooksBookshelf, on_delete=models.CASCADE)
    class Meta:
        managed = False
        db_table = 'books_book_bookshelves'

class BooksBookLanguages(models.Model):
    id = models.IntegerField(primary_key=True)
    book = models.ForeignKey(BooksBook, on_delete=models.CASCADE)
    language = models.ForeignKey(BooksLanguage, on_delete=models.CASCADE)
    class Meta:
        managed = False
        db_table = 'books_book_languages'

class BooksBookSubjects(models.Model):
    id = models.IntegerField(primary_key=True)
    book = models.ForeignKey(BooksBook, on_delete=models.CASCADE)
    subject = models.ForeignKey(BooksSubject, on_delete=models.CASCADE)
    class Meta:
        managed = False
        db_table = 'books_book_subjects'




