# Generated by Django 4.0.2 on 2022-11-03 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('total_statistics', '0025_statistics_returnpercentage'),
    ]

    operations = [
        migrations.AddField(
            model_name='statistics',
            name='highestLossReturnPct',
            field=models.CharField(default=1, max_length=255, verbose_name='highestLossReturnPct'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='statistics',
            name='highestWinReturnPct',
            field=models.CharField(default=1, max_length=255, verbose_name='highestWinReturnPct'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='statistics',
            name='lossReturnPercentage',
            field=models.CharField(default=1, max_length=255, verbose_name='lossReturnPercentage'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='statistics',
            name='lowestLossReturnPct',
            field=models.CharField(default=1, max_length=255, verbose_name='lowestLossReturnPct'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='statistics',
            name='lowestWinReturnPct',
            field=models.CharField(default=1, max_length=255, verbose_name='lowestWinReturnPct'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='statistics',
            name='winsReturnPercentage',
            field=models.CharField(default=1, max_length=255, verbose_name='winsReturnPercentage'),
            preserve_default=False,
        ),
    ]