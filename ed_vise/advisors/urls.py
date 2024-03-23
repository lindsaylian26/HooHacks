app_name = 'advisors'
from django.urls import path
from . import views
from .views import AdvisorList

urlpatterns = [
    path('register/', views.register_advisor, name='register'),
    path('profile/<int:advisor_id>/', views.advisor_profile, name='advisor_profile'),
    path('api/advisors/', AdvisorList.as_view(), name='advisor-list')

]