# Generated by Django 5.1 on 2024-09-06 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_remove_aboutus_why_choose_us_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tour',
            name='description_en',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tour',
            name='description_hy',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tour',
            name='description_ru',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tour',
            name='duration_en',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='tour',
            name='duration_hy',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='tour',
            name='duration_ru',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='tour',
            name='location_en',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='tour',
            name='location_hy',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='tour',
            name='location_ru',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='tour',
            name='name_en',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='tour',
            name='name_hy',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='tour',
            name='name_ru',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
