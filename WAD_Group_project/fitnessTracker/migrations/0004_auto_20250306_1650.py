# Generated by Django 2.1.5 on 2025-03-06 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitnessTracker', '0003_auto_20250306_1641'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercise',
            name='slug',
            field=models.SlugField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='workout',
            name='slug',
            field=models.SlugField(default=''),
            preserve_default=False,
        ),
    ]
