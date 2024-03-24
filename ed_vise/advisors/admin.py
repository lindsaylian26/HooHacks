from django.contrib import admin
# Register your models here.
from .models import Advisor


class AdvisorAdmin(admin.ModelAdmin):
    model = Advisor
    filter_horizontal = ('subjects',)  # Use filter_horizontal for better UI in case of ManyToManyField

admin.site.register(Advisor, AdvisorAdmin)