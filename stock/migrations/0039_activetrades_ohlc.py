# Generated by Django 4.0.2 on 2022-09-07 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0038_activetrades_durationoftrade'),
    ]

    operations = [
        migrations.AddField(
            model_name='activetrades',
            name='ohlc',
            field=models.JSONField(null=True),
        ),
    ]
