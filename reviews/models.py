from django.conf import settings
from django.db import models

class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    stars = models.CharField(max_length=1, choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], blank=True, null=True)
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user_image = models.ImageField(upload_to='user_images', blank= True, null=True)
    comment_image = models.ImageField(upload_to='comment_images', blank=True, null=True)

    def __str__(self):
        return f"Review by {self.user.username if self.user else 'Anonymous'}"
