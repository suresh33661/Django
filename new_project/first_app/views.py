from django.shortcuts import render


# Create your views here.
from django.http import HttpResponse

def homepage(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')