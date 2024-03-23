# ed_vise/views.py

from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the Ed-Vise homepage!")
