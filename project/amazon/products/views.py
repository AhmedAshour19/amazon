from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):

    return HttpResponse("Hello from section 1 -django heros")

def index2(request):

    return HttpResponse("WELCOME")

def index3(request):

    return HttpResponse("Hello students of the College of Artificial Intelligence")