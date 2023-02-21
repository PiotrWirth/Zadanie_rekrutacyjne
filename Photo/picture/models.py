from django.db import models
from django.conf import settings
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill


# Create your models here.

class Picture(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images')
    thumbnail200x200 = ImageSpecField(source='image', processors=[ResizeToFill(200, 200)], format="PNG", options={'quality': 60})
    thumbnail400x400 = ImageSpecField(source='image', processors=[ResizeToFill(400, 400)], format="PNG", options={'quality': 60})
    created_at = models.TimeField(auto_now=True)
    
    