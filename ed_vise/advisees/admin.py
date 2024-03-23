from django.contrib import admin
from .models import SubjectArea  # Adjust the import path as needed

@admin.register(SubjectArea)
class SubjectAreaAdmin(admin.ModelAdmin):
    list_display = ['name']  
