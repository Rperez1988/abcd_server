# Generated by Django 4.0.2 on 2022-11-08 07:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('total_statistics', '0028_remove_statistics_active_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='statistics',
            old_name='longWinPct',
            new_name='shortStartPnl',
        ),
    ]