from django.db import models
from django.conf import settings
from datetime import timedelta

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    tier = models.CharField(max_length=10)
    time_passed = models.DurationField(default=timedelta)

    def __str__(self):
        return self.user.username
