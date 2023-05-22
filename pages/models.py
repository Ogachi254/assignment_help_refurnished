from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.name

class Order(models.Model):
    email = models.EmailField()
    order_title = models.CharField(max_length=255, default='Default Title')
    subject = models.CharField(max_length=255)
    deadline = models.DateTimeField()
    instructions = models.TextField()
    documents = models.FileField(upload_to='order/documents/', blank=True, null=True)
    images = models.FileField(upload_to='order/images/', blank=True, null=True)
    folders = models.FileField(upload_to='order/folders/', blank=True, null=True)

    def __str__(self):
        return self.order_title
