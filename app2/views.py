from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def first(request):
    return HttpResponse('<h1>Give me one chance i will prove my self daddy</h1>')

def second(request):
    return HttpResponse('<marquee><h1>Thank you soo much for giving this life mom and daddy</h1></marquee>')
