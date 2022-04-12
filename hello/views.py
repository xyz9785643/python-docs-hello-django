from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return HttpResponse("Hello DXC Team - Good Morning, How are you ? Today we are happy & we are learning Cloud Concepts")
