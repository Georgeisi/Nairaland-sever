# Generated by Django 4.2.3 on 2023-07-26 13:30

import cloudinary.models
from django.db import migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_blogpost_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='image',
            field=cloudinary.models.CloudinaryField(default=django.utils.timezone.now, max_length=255, verbose_name='image'),
            preserve_default=False,
        ),
    ]
