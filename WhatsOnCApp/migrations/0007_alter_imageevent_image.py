# Generated by Django 4.2.23 on 2025-07-11 17:07

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('WhatsOnCApp', '0006_alter_imageevent_event'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imageevent',
            name='image',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='imageE'),
        ),
    ]
