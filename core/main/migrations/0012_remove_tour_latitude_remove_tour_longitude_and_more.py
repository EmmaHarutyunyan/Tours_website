# Generated by Django 5.1 on 2024-08-30 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_remove_tour_location_address_tour_latitude_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tour',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='tour',
            name='longitude',
        ),
        migrations.AddField(
            model_name='tour',
            name='location_address',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
