# ed_vise/views.py

from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'ed_vise/home.html')
