from django.urls import path
from . import views

urlpatterns = [
    path('google_login/', views.google_login, name='google_login'),
    path('oauth2callback/', views.oauth2callback, name = 'oauth2callback'),
    # Other URL patterns...
]
