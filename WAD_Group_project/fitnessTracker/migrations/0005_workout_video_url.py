# Generated by Django 2.1.5 on 2025-03-22 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitnessTracker', '0004_meal_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='workout',
            name='video_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
