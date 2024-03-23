from django.urls import path
from . import views

urlpatterns = [
    path('events/', views.event_list, name='event_list'),
    # Add more URL patterns as needed
]
