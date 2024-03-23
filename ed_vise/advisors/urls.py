app_name = 'advisors'
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_advisor, name='register'),
    path('profile/<int:advisor_id>/', views.advisor_profile, name='advisor_profile'),
]
