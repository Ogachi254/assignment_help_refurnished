from django.conf import settings
from django.db import models

class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    text = models.TextField()
    image = models.ImageField(upload_to='post_images', blank=True, null=True)

    def __str__(self):
        return self.text[:50]