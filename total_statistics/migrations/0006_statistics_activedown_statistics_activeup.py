# Generated by Django 4.0.2 on 2022-10-14 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('total_statistics', '0005_statistics_averagereward'),
    ]

    operations = [
        migrations.AddField(
            model_name='statistics',
            name='activeDown',
            field=models.CharField(default=1, max_length=255, verbose_name='activeDown'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='statistics',
            name='activeUp',
            field=models.CharField(default=1, max_length=255, verbose_name='activeUp'),
            preserve_default=False,
        ),
    ]