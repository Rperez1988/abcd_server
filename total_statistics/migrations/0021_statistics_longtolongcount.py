# Generated by Django 4.0.2 on 2022-10-31 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('total_statistics', '0020_statistics_longendcount'),
    ]

    operations = [
        migrations.AddField(
            model_name='statistics',
            name='longToLongCount',
            field=models.CharField(default=1, max_length=255, verbose_name='longToLongCount'),
            preserve_default=False,
        ),
    ]
