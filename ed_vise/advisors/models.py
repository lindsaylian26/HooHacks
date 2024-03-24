from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save  # This import is required for post_save
from django.dispatch import receiver  # This import is required for the receiver decorator
from advisees.models import SubjectArea

class Advisor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    subjects = models.ManyToManyField('advisees.SubjectArea')  # Adjust the model name if necessary
    availability = models.CharField(max_length=255)
    is_advisor = models.BooleanField(default=True)
    name = models.CharField(max_length=100, default='')  # Set default value to an empty string

    def __str__(self):
        return self.name


    
class Subject(models.Model):
    name = models.CharField(max_length=100)
    # any other fields...

    def __str__(self):
        return self.name

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    is_advisor = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
 # Automatically create a Profile when a User is created
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()