app_name='advisors'
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_advisee, name='register'),
    path('profile/<int:advisee_id>/', views.advisee_profile, name='advisee_profile'),
]
