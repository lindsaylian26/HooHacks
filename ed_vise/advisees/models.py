from django.db import models
from django.contrib.auth.models import User
from advisors.models import Advisor

class Advisee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    subject_needed = models.ForeignKey('advisees.SubjectArea', on_delete=models.SET_NULL, null=True)
    availability = models.CharField(max_length=255)
    advisor = models.ForeignKey('advisors.Advisor', on_delete=models.SET_NULL, null=True)



class SubjectArea(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name