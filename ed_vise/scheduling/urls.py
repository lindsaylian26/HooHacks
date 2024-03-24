from django.urls import path, include
from . import views

urlpatterns = [
    path('google_login/', views.google_login, name='google_login'),
    path('oauth2callback/', views.oauth2callback, name = 'oauth2callback'),
    path('events/', views.list_events, name='list-events'),
    path('events/', views.list_events, name='events'),
    path('google-login/', views.google_login, name='google_login'),
]
