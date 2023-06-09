# Generated by Django 4.2.1 on 2023-05-25 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_commentimage_image_comment_post_images'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='images',
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='post_images'),
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='CommentImage',
        ),
        migrations.DeleteModel(
            name='Image',
        ),
    ]
