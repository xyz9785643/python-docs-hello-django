from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return HttpResponse("Hello POWERBI Team - Good Morning, How are you ? !")
