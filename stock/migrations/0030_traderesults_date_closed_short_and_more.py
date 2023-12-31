# Generated by Django 4.0.2 on 2022-08-08 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0029_remove_traderesults_date_closed_short_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='traderesults',
            name='date_closed_short',
            field=models.CharField(default=1, max_length=255, verbose_name='date_closed_short'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='traderesults',
            name='date_entered_short',
            field=models.CharField(default=1, max_length=255, verbose_name='date_entered_short'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='traderesults',
            name='date_of_pivot_high',
            field=models.CharField(default=1, max_length=255, verbose_name='date_of_pivot_high'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='traderesults',
            name='date_of_pivot_low',
            field=models.CharField(default=1, max_length=255, verbose_name='date_of_pivot_low'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='traderesults',
            name='date_pivot_high_snr_tested',
            field=models.CharField(default=1, max_length=255, verbose_name='date_pivot_high_snr_tested'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='traderesults',
            name='high_close_mark',
            field=models.CharField(default=1, max_length=255, verbose_name='high_close_mark'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='traderesults',
            name='highest_price_went',
            field=models.CharField(default=1, max_length=255, verbose_name='highest_price_went'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='traderesults',
            name='low_close_mark',
            field=models.CharField(default=1, max_length=255, verbose_name='low_close_mark'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='traderesults',
            name='lowest_price_went',
            field=models.CharField(default=1, max_length=255, verbose_name='lowest_price_went'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='traderesults',
            name='pair_range',
            field=models.CharField(default=1, max_length=255, verbose_name='pair_range'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='traderesults',
            name='pivot_pair',
            field=models.CharField(default=1, max_length=255, verbose_name='pivot_pair'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='traderesults',
            name='pnl',
            field=models.CharField(default=1, max_length=255, verbose_name='pnl'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='traderesults',
            name='price_closed_short',
            field=models.CharField(default=1, max_length=255, verbose_name='price_closed_short'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='traderesults',
            name='price_entered_short',
            field=models.CharField(default=1, max_length=255, verbose_name='price_entered_short'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='traderesults',
            name='price_of_pivot_high',
            field=models.CharField(default=1, max_length=255, verbose_name='price_of_pivot_high'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='traderesults',
            name='price_of_pivot_low',
            field=models.CharField(default=1, max_length=255, verbose_name='price_of_pivot_low'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='traderesults',
            name='price_pivot_high_snr_tested',
            field=models.CharField(default=1, max_length=255, verbose_name='price_pivot_high_snr_tested'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='traderesults',
            name='stock',
            field=models.CharField(default=1, max_length=255, verbose_name='stock'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='traderesults',
            name='trade_complete',
            field=models.CharField(default=1, max_length=255, verbose_name='trade_complete'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='traderesults',
            name='trade_result',
            field=models.CharField(default=1, max_length=255, verbose_name='trade_result'),
            preserve_default=False,
        ),
    ]
