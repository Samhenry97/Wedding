from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import RegexValidator, MaxValueValidator, MinValueValidator
from datetime import datetime

class RSVP(models.Model):
    name = models.CharField(max_length=256)
    email = models.EmailField()
    number = models.IntegerField(default=1)
    message = models.TextField(max_length=1024)
    attending = models.CharField(max_length=256, default='Both')
    created = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return '{} ({}): {}'.format(self.name, self.email, self.number)


class Profile(models.Model):
    """
    The profile model, which contains extra data besides the
    Django defaults for a user.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    records_per_page = models.IntegerField(default=25, validators=[
        MaxValueValidator(100),  # No more than 100 records per page
        MinValueValidator(1)  # No less than 1 record per page
    ])

    def __str__(self):
        """Returns a textual representation of the user, the username"""
        return self.user.username

    def full_name(self):
        """Returns the user's full name, first + last"""
        return '{} {}'.format(self.user.first_name, self.user.last_name)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """Creates the user profile whenever a user is created"""
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    """Saves the user profile whenever the user is saved"""
    instance.profile.save()
