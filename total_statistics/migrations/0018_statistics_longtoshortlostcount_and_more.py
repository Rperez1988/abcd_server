# Generated by Django 4.0.2 on 2022-10-19 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('total_statistics', '0017_statistics_shortendlost_statistics_shortendpnl_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='statistics',
            name='longToShortLostCount',
            field=models.CharField(default=1, max_length=255, verbose_name='longToShortLostCount'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='statistics',
            name='longToShortPnl',
            field=models.CharField(default=1, max_length=255, verbose_name='longToShortPnl'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='statistics',
            name='longToShortWinCount',
            field=models.CharField(default=1, max_length=255, verbose_name='longToShortWinCount'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='statistics',
            name='longToShortWinPct',
            field=models.CharField(default=1, max_length=255, verbose_name='longToShortWinPct'),
            preserve_default=False,
        ),
    ]