# Generated by Django 2.2.28 on 2025-03-15 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitnessTracker', '0003_userprofile_favourites'),
    ]

    operations = [
        migrations.AddField(
            model_name='meal',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
