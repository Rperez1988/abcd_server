# Generated by Django 4.0.2 on 2023-06-21 03:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('access_trades', '0005_rename_filtered_trade_trades_in_chart_view'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='trades_in_chart_view',
            new_name='TradesInChartView',
        ),
    ]
