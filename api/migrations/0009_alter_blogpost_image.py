# Generated by Django 4.2.3 on 2023-07-26 16:11

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_alter_blogpost_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='image',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='image'),
        ),
    ]
