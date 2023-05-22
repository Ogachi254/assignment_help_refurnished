from datetime import timezone
from django.utils import timezone
from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.name


class Order(models.Model):
    order_title = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    paper_title = models.CharField(max_length=100, default="Unknown")
    academic_level = models.CharField(max_length=100, default="")
    language = models.CharField(max_length=100, default="English")
    formatting_style = models.CharField(max_length=100, default="APA")
    pages = models.IntegerField(default=0)
    sources = models.IntegerField(default=0)
    deadline = models.DateTimeField(default=timezone.now)
    budget = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    instructions = models.TextField(default="")
    documents = models.FileField(upload_to='documents/', default='default_document.pdf')
    images = models.FileField(upload_to='images/', default='default_image.jpg', blank=True)
    folders = models.FileField(upload_to='folders/', default='default_folder.zip', blank=True)
    email = models.EmailField(default='example@example.com')

    def __str__(self):
        return self.order_title

