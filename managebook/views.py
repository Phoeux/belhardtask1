from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

# def hello(request):
#     return HttpResponse('Hello world')

def hello(request):
    response = {'user': 'Gleb'}
    return render(request, 'index.html', response)
