# Generated by Django 5.1 on 2024-08-31 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_remove_tour_end_time_remove_tour_location_address_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tour',
            name='end_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tour',
            name='location',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='tour',
            name='start_time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]