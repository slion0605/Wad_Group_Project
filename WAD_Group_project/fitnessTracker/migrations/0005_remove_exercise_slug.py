# Generated by Django 2.1.5 on 2025-03-06 16:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fitnessTracker', '0004_auto_20250306_1650'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exercise',
            name='slug',
        ),
    ]
