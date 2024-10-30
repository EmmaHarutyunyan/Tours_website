# Generated by Django 5.1 on 2024-09-02 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_aboutus'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aboutus',
            name='why_choose_us',
        ),
        migrations.AddField(
            model_name='aboutus',
            name='authentic_experiences',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='expert_guides',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='personalized_itineraries',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='aboutus',
            name='mission',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='aboutus',
            name='our_story',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='aboutus',
            name='why_choose_armenia',
            field=models.TextField(blank=True, null=True),
        ),
    ]
