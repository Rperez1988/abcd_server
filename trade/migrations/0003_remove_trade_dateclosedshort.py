# Generated by Django 4.0.2 on 2022-09-17 02:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trade', '0002_rename_ohlc_trade_chartdata_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trade',
            name='dateClosedShort',
        ),
    ]
