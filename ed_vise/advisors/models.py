from django.db import models
from django.contrib.auth.models import User

class Advisor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    subjects = models.ManyToManyField('Subject', related_name='advisors')
    availability = models.CharField(max_length=255)

class SubjectArea(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
