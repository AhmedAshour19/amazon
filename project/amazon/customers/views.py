from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):

    return HttpResponse(f"Welcome, customers, to the page ' index '")

def index2(request):

    return HttpResponse(f"Welcome, customers, to the page ' index2 '")

def index3(request):

    return HttpResponse(f"Welcome, customers, to the page ' index3 '")
