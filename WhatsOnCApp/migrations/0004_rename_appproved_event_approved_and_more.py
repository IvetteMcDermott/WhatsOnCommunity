# Generated by Django 4.2.23 on 2025-06-16 14:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('WhatsOnCApp', '0003_event_appproved_event_description_provider_approved_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='appproved',
            new_name='approved',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='date',
            new_name='endDate',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='time',
            new_name='endTime',
        ),
        migrations.AddField(
            model_name='event',
            name='startDate',
            field=models.DateField(default='2025-01-01'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='startTime',
            field=models.TimeField(default='00:00'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=15, unique=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WhatsOnCApp.category'),
        ),
        migrations.AlterField(
            model_name='event',
            name='provider',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WhatsOnCApp.provider'),
        ),
    ]
