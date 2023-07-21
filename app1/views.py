from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def first(request):
    return HttpResponse('<marquee><h1>I love you soo much mom and daddy</h1></marquee>')

def second(request):
    return HttpResponse('<h1>Thank you soo much for giving this life mom</h1>')
