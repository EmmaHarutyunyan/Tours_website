# Generated by Django 5.1 on 2024-08-31 14:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_rename_latitude_tour_end_lat_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tour',
            name='end_lat',
        ),
        migrations.RemoveField(
            model_name='tour',
            name='end_lng',
        ),
        migrations.RemoveField(
            model_name='tour',
            name='end_place',
        ),
        migrations.RemoveField(
            model_name='tour',
            name='middle_lat',
        ),
        migrations.RemoveField(
            model_name='tour',
            name='middle_lng',
        ),
        migrations.RemoveField(
            model_name='tour',
            name='middle_place',
        ),
        migrations.RemoveField(
            model_name='tour',
            name='start_lat',
        ),
        migrations.RemoveField(
            model_name='tour',
            name='start_lng',
        ),
        migrations.RemoveField(
            model_name='tour',
            name='start_place',
        ),
    ]
