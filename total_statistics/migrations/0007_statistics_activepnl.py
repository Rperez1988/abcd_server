# Generated by Django 4.0.2 on 2022-10-14 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('total_statistics', '0006_statistics_activedown_statistics_activeup'),
    ]

    operations = [
        migrations.AddField(
            model_name='statistics',
            name='activePnl',
            field=models.CharField(default=1, max_length=255, verbose_name='activePnl'),
            preserve_default=False,
        ),
    ]
