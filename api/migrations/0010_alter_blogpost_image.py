# Generated by Django 4.2.3 on 2023-07-26 16:23

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_alter_blogpost_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='image',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='https://res.cloudinary.com/dpoix2ilz/image'),
        ),
    ]
