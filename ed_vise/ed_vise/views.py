# ed_vise/views.py

from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'ed_vise/home.html')

def set_session(request):
    request.session['user_id'] = 123
    return HttpResponse("Session set successfully")

def get_session(request):
    user_id = request.session.get('user_id')
    return HttpResponse(f"User ID from session: {user_id}")