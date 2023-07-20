# Generated by Django 4.0.2 on 2022-11-08 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('total_statistics', '0032_statistics_totalavgreturn'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='statistics',
            name='cryptoCount',
        ),
        migrations.RemoveField(
            model_name='statistics',
            name='forexCount',
        ),
        migrations.RemoveField(
            model_name='statistics',
            name='nasdaqCount',
        ),
        migrations.RemoveField(
            model_name='statistics',
            name='optionsCount',
        ),
        migrations.AddField(
            model_name='statistics',
            name='cryptoActiveCount',
            field=models.CharField(default=1, max_length=255, verbose_name='cryptoActiveCount'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='statistics',
            name='cryptoClosedCount',
            field=models.CharField(default=1, max_length=255, verbose_name='cryptoClosedCount'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='statistics',
            name='cryptoTotalCount',
            field=models.CharField(default=1, max_length=255, verbose_name='cryptoTotalCount'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='statistics',
            name='forexActiveCount',
            field=models.CharField(default=1, max_length=255, verbose_name='forexActiveCount'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='statistics',
            name='forexClosedCount',
            field=models.CharField(default=1, max_length=255, verbose_name='forexClosedCount'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='statistics',
            name='forexTotalCount',
            field=models.CharField(default=1, max_length=255, verbose_name='forexTotalCount'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='statistics',
            name='nasdaqActiveCount',
            field=models.CharField(default=1, max_length=255, verbose_name='nasdaqActiveCount'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='statistics',
            name='nasdaqClosedCount',
            field=models.CharField(default=1, max_length=255, verbose_name='nasdaqClosedCount'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='statistics',
            name='nasdaqTotalCount',
            field=models.CharField(default=1, max_length=255, verbose_name='nasdaqTotalCount'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='statistics',
            name='optionsActiveCount',
            field=models.CharField(default=1, max_length=255, verbose_name='optionsActiveCount'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='statistics',
            name='optionsClosedCount',
            field=models.CharField(default=1, max_length=255, verbose_name='optionsClosedCount'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='statistics',
            name='optionsTotalCount',
            field=models.CharField(default=1, max_length=255, verbose_name='optionsTotalCount'),
            preserve_default=False,
        ),
    ]
