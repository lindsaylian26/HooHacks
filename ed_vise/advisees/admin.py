from django.contrib import admin
from .models import SubjectArea, Advisor  # Adjust the import path as needed

@admin.register(SubjectArea)
class SubjectAreaAdmin(admin.ModelAdmin):
    list_display = ['name']  


@admin.register(Advisor)
class AdvisorAdmin(admin.ModelAdmin):
    list_display = ['name']  