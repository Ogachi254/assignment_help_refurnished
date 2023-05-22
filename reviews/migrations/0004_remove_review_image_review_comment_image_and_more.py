# Generated by Django 4.2.1 on 2023-05-20 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_review_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='image',
        ),
        migrations.AddField(
            model_name='review',
            name='comment_image',
            field=models.ImageField(blank=True, null=True, upload_to='comment_images'),
        ),
        migrations.AddField(
            model_name='review',
            name='user_image',
            field=models.ImageField(blank=True, null=True, upload_to='user_images'),
        ),
    ]