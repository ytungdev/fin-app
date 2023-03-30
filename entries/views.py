from django.shortcuts import render
from django.http import HttpResponse

def entries(request):
    return HttpResponse("Hello world!")