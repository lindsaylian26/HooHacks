from django.contrib import admin
# Register your models here.
from .models import Advisor


class AdvisorAdmin(admin.ModelAdmin):
    list_display = ['name']  
    model = Advisor
    filter_horizontal = ('subjects',)  # Use filter_horizontal for better UI in case of ManyToManyField

    def __str__(self):
        return self.name

admin.site.register(Advisor, AdvisorAdmin)