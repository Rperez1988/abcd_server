# Generated by Django 4.0.2 on 2023-02-06 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trade', '0018_trade_settingsname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trade',
            name='settings',
        ),
        migrations.AddField(
            model_name='trade',
            name='info',
            field=models.JSONField(null=True),
        ),
    ]
