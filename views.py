from django.shortcuts import render
from django.http import HttpResponse

def cse(request):
    return HttpResponse("Welcome to CSE page") 
def etc(request):
    return HttpResponse("Welcome to ETC page")
def mech(request):
    return HttpResponse("Welcome to Mech page")
def civil(request):
    return HttpResponse("Welcome to Civil page")            


