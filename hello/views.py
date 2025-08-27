from django.shortcuts import render
#As we want to send a perticular response we have to import the following file
from django.http import HttpResponse
# Create your views here.
def hello(request):
    return HttpResponse("<h1>Welcome to DJango 5.2</h1>")
def hii(request):
    return HttpResponse("<h4>Hello World</h4>")
