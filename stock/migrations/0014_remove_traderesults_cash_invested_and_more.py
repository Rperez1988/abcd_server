# Generated by Django 4.0.2 on 2022-05-19 05:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0013_traderesults_price_pivot_high_snr_tested'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='traderesults',
            name='cash_invested',
        ),
        migrations.RemoveField(
            model_name='traderesults',
            name='current_cash_in_hand',
        ),
        migrations.RemoveField(
            model_name='traderesults',
            name='shares_purchased',
        ),
    ]
