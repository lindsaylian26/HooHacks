from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_advisee, name='register_advisee'),
    path('profile/<int:advisee_id>/', views.advisee_profile, name='advisee_profile'),
]
