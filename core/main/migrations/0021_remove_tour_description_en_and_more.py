# Generated by Django 5.1 on 2024-09-06 12:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_tour_description_en_tour_description_hy_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tour',
            name='description_en',
        ),
        migrations.RemoveField(
            model_name='tour',
            name='description_hy',
        ),
        migrations.RemoveField(
            model_name='tour',
            name='description_ru',
        ),
        migrations.RemoveField(
            model_name='tour',
            name='duration_en',
        ),
        migrations.RemoveField(
            model_name='tour',
            name='duration_hy',
        ),
        migrations.RemoveField(
            model_name='tour',
            name='duration_ru',
        ),
        migrations.RemoveField(
            model_name='tour',
            name='location_en',
        ),
        migrations.RemoveField(
            model_name='tour',
            name='location_hy',
        ),
        migrations.RemoveField(
            model_name='tour',
            name='location_ru',
        ),
        migrations.RemoveField(
            model_name='tour',
            name='name_en',
        ),
        migrations.RemoveField(
            model_name='tour',
            name='name_hy',
        ),
        migrations.RemoveField(
            model_name='tour',
            name='name_ru',
        ),
    ]
