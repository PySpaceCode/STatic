from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def hello_shoe(request):
    return HttpResponse("<h1>This is my first heading | page</h1>")
def aman(rq):
    return HttpResponse("<h1>Thi9s is my first views</h1>")