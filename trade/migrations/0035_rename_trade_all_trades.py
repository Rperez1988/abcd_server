# Generated by Django 4.0.2 on 2023-06-19 06:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trade', '0034_remove_trade_barlocations_remove_trade_bcretracement_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='trade',
            new_name='all_trades',
        ),
    ]