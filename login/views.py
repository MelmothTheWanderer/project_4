from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def login_index(request):
    return HttpResponse('This will be the login page')