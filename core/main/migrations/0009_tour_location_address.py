# Generated by Django 5.1 on 2024-08-30 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_remove_video_caption'),
    ]

    operations = [
        migrations.AddField(
            model_name='tour',
            name='location_address',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]