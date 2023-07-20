# Generated by Django 4.0.2 on 2022-10-29 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('total_statistics', '0018_statistics_longtoshortlostcount_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='statistics',
            name='longToLongLostCount',
            field=models.CharField(default=1, max_length=255, verbose_name='longToLongLostCount'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='statistics',
            name='longToLongPnl',
            field=models.CharField(default=1, max_length=255, verbose_name='longToLongPnl'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='statistics',
            name='longToLongWinCount',
            field=models.CharField(default=1, max_length=255, verbose_name='longToLongWinCount'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='statistics',
            name='longToLongWinPct',
            field=models.CharField(default=1, max_length=255, verbose_name='longToLongWinPct'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='statistics',
            name='shortToLongLostCount',
            field=models.CharField(default=1, max_length=255, verbose_name='shortToLongLostCount'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='statistics',
            name='shortToLongPnl',
            field=models.CharField(default=1, max_length=255, verbose_name='shortToLongPnl'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='statistics',
            name='shortToLongWinCount',
            field=models.CharField(default=1, max_length=255, verbose_name='shortToLongWinCount'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='statistics',
            name='shortToLongWinPct',
            field=models.CharField(default=1, max_length=255, verbose_name='shortToLongWinPct'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='statistics',
            name='shortToShortLostCount',
            field=models.CharField(default=1, max_length=255, verbose_name='shortToShortLostCount'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='statistics',
            name='shortToShortPnl',
            field=models.CharField(default=1, max_length=255, verbose_name='shortToShortPnl'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='statistics',
            name='shortToShortWinCount',
            field=models.CharField(default=1, max_length=255, verbose_name='shortToShortWinCount'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='statistics',
            name='shortToShortWinPct',
            field=models.CharField(default=1, max_length=255, verbose_name='shortToShortWinPct'),
            preserve_default=False,
        ),
    ]
