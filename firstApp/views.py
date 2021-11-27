from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def index(request):
    data = { "variable": "Books Page" }
    return render(request, 'index.html', data)

@csrf_exempt
def getBooks(request):

    try:
        
        
        data = { "variable": "Books Page" }






    except Exception as e:
        raise e
    
    return JsonResponse(data)