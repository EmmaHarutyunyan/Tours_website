# Generated by Django 5.1 on 2024-09-02 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_remove_tour_end_lat_remove_tour_end_lng_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mission', models.TextField()),
                ('why_choose_us', models.TextField()),
                ('our_story', models.TextField()),
                ('why_choose_armenia', models.TextField()),
            ],
        ),
    ]
