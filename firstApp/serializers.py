from rest_framework import serializers
from .models import BooksBook, BooksFormat, BooksAuthor, BooksBookshelf, BooksLanguage, BooksSubject

class BooksAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = BooksAuthor
        fields = ['id', 'birth_year', 'death_year', 'name']

class BooksBookshelfSerializer(serializers.ModelSerializer):
    class Meta:
        model = BooksBookshelf
        fields = ['id', 'name']

class BooksLanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = BooksLanguage
        fields = ['id', 'code']

class BooksSubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = BooksSubject
        fields = ['id', 'name']

class BooksFormatSerializer(serializers.ModelSerializer):
    class Meta:
        model = BooksFormat
        fields = ['id', 'mime_type', 'url', 'book']

class BooksBookSerializer(serializers.ModelSerializer):
    formats = BooksFormatSerializer(many=True, read_only=True)
    authors = BooksAuthorSerializer(many=True, read_only=True)
    bookshelfs = BooksBookshelfSerializer(many=True, read_only=True)
    languages = BooksLanguageSerializer(many=True, read_only=True)
    subjects = BooksSubjectSerializer(many=True, read_only=True)

    class Meta:
        model = BooksBook
        fields = ['id', 'download_count', 'gutenberg_id', 'media_type', 'title', 'formats', 'authors', 'bookshelfs', 'languages', 'subjects']
