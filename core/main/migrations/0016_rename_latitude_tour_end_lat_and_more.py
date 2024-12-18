# Generated by Django 5.1 on 2024-08-31 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_tour_latitude_tour_longitude'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tour',
            old_name='latitude',
            new_name='end_lat',
        ),
        migrations.RenameField(
            model_name='tour',
            old_name='longitude',
            new_name='end_lng',
        ),
        migrations.AddField(
            model_name='tour',
            name='end_place',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='tour',
            name='middle_lat',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tour',
            name='middle_lng',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tour',
            name='middle_place',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='tour',
            name='start_lat',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tour',
            name='start_lng',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tour',
            name='start_place',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
