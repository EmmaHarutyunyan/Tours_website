# Generated by Django 5.1 on 2024-08-30 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_tour_location_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='tour',
            name='end_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tour',
            name='start_time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
