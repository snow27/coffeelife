from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, 'home/index.html')

def columbia(request):
    return render(request, 'home/columbia.html')
