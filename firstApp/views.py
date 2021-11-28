from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
from .serializers import BooksBookSerializer
from rest_framework.renderers import JSONRenderer
import json 

#models
from firstApp.models import BooksAuthor, BooksLanguage, BooksSubject, BooksFormat, BooksBookshelf, BooksBookSubjects, BooksBookLanguages, BooksBookBookshelves, BooksBookAuthors, BooksBook

# Create your views here.
def index(request):
    data = { "variable": "Books" }
    return render(request, 'index.html', data)

@csrf_exempt
def getBooks(request):

    try:

        # retive all formData
        formData = {
            "page_number" : int(request.POST.get('page_number')),
            "lang_codes" : request.POST.get('lang_codes'),
            "bookID" : request.POST.get('bookID'),
            "title" : request.POST.get('title'),
            "author" : request.POST.get('author'),
            "sob" : request.POST.get('sob'),
            "mime" : request.POST.get('mime'),
        }

        ### Retrieve all books by reverse order of downloads
        books = BooksBook.objects.all().order_by('-download_count').distinct()

        if(formData['bookID']):
            books = books.filter(gutenberg_id=formData['bookID'])

        if(formData['title']):
            books = books.filter(title__icontains=formData['title'])

        if(formData['mime']):
            books = books.filter(booksformat__mime_type__icontains=formData['mime'])

        if(formData['author']):
            books = books.filter(authors__name__icontains=formData['author'])

        if(formData['sob']):
            books = books.filter(Q(subjects__name__icontains=formData['sob']) | Q(bookshelfs__name__icontains=formData['sob']))
            
        if(formData['lang_codes']):
            formData['lang_codes'] = formData['lang_codes'].split(",")
            books = books.filter(languages__code__in=formData['lang_codes'])

        # paginator = Paginator(books, 25)
        # page_obj = paginator.page(formData['page_number'])

        total_books=books.count()
        
        ### Manual - pagination
        start = 0 if (formData['page_number'] == 1) else (formData['page_number'] - 1) * 25
        end = formData['page_number']*25
        books = books[start:end] 

        serialzr = BooksBookSerializer(books, many=True)
        jsonData = JSONRenderer().render(serialzr.data)

        data = {
            "total_books" : total_books,
            "page_number" : formData['page_number'],
            "page_obj" : json.loads(jsonData),
        }

    except Exception as e:
        raise e
    
    return JsonResponse(data, safe=False)


@csrf_exempt
def getLanguages(request):

    try:
        
        languages = BooksLanguage.objects.all()

    except Exception as e:
        raise e
    
    return JsonResponse(list(languages.values()), safe=False)