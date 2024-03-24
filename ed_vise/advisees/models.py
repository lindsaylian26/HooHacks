from django.db import models
from django.contrib.auth.models import User
from django.apps import apps


class Advisee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    subject_needed = models.ForeignKey('advisees.SubjectArea', on_delete=models.SET_NULL, null=True)
    availability = models.CharField(max_length=255)
    
    def get_advisor_model(self):
        return apps.get_model('advisors', 'Advisor')



class SubjectArea(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name