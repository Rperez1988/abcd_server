# Generated by Django 4.0.2 on 2022-11-08 08:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('total_statistics', '0029_rename_longwinpct_statistics_shortstartpnl'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='statistics',
            name='longEndsCount',
        ),
        migrations.RemoveField(
            model_name='statistics',
            name='longStartsCount',
        ),
        migrations.RemoveField(
            model_name='statistics',
            name='shortEndsCount',
        ),
        migrations.RemoveField(
            model_name='statistics',
            name='shortStartsCount',
        ),
    ]