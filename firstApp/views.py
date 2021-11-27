from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator

#models
from firstApp.models import BooksAuthor, BooksLanguage, BooksSubject, BooksFormat, BooksBookshelf, BooksBookSubjects, BooksBookLanguages, BooksBookBookshelves, BooksBookAuthors, BooksBook

# Create your views here.
def index(request):
    data = { "variable": "Books" }
    return render(request, 'index.html', data)

@csrf_exempt
def getBooks(request):

    try:
        page_number = int(request.POST.get('page_number'))
        
        books = BooksBook.objects.all().order_by('-download_count').values()


        paginator = Paginator(books, 25)
        page_obj = paginator.get_page(page_number)

        data = {
            "page_obj" : list(page_obj),
            "page_number" : page_number
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