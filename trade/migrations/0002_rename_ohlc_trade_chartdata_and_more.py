# Generated by Django 4.0.2 on 2022-09-17 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trade', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='trade',
            old_name='ohlc',
            new_name='chartData',
        ),
        migrations.RenameField(
            model_name='trade',
            old_name='durationOfTrade',
            new_name='tradeType',
        ),
        migrations.RemoveField(
            model_name='trade',
            name='a_close_mark',
        ),
        migrations.RemoveField(
            model_name='trade',
            name='activePrice',
        ),
        migrations.RemoveField(
            model_name='trade',
            name='b_close_mark',
        ),
        migrations.RemoveField(
            model_name='trade',
            name='date_entered_short',
        ),
        migrations.RemoveField(
            model_name='trade',
            name='date_of_pivot_A',
        ),
        migrations.RemoveField(
            model_name='trade',
            name='date_of_pivot_B',
        ),
        migrations.RemoveField(
            model_name='trade',
            name='date_supp_resistance_tested',
        ),
        migrations.RemoveField(
            model_name='trade',
            name='market',
        ),
        migrations.RemoveField(
            model_name='trade',
            name='price_entered_short',
        ),
        migrations.RemoveField(
            model_name='trade',
            name='price_of_pivot_A',
        ),
        migrations.RemoveField(
            model_name='trade',
            name='price_of_pivot_B',
        ),
        migrations.RemoveField(
            model_name='trade',
            name='price_supp_resistance_tested',
        ),
        migrations.RemoveField(
            model_name='trade',
            name='status',
        ),
        migrations.RemoveField(
            model_name='trade',
            name='symbol',
        ),
        migrations.RemoveField(
            model_name='trade',
            name='tradeid',
        ),
        migrations.AddField(
            model_name='trade',
            name='currentDate',
            field=models.CharField(default=1, max_length=255, verbose_name='currentDate'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='trade',
            name='currentPrice',
            field=models.CharField(default=1, max_length=255, verbose_name='currentPrice'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='trade',
            name='dateClosedShort',
            field=models.CharField(default=1, max_length=255, verbose_name='dateClosedShort'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='trade',
            name='dateEnteredShort',
            field=models.CharField(default=1, max_length=255, verbose_name='dateEnteredShort'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='trade',
            name='dateOfA',
            field=models.CharField(default=1, max_length=255, verbose_name='dateOfA'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='trade',
            name='dateofB',
            field=models.CharField(default=1, max_length=255, verbose_name='dateofB'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='trade',
            name='daysSinceStartDate',
            field=models.CharField(default=1, max_length=255, verbose_name='daysSinceStartDate'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='trade',
            name='furthestOfA',
            field=models.CharField(default=1, max_length=255, verbose_name='furthestOfA'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='trade',
            name='pivotPair',
            field=models.CharField(default=1, max_length=255, verbose_name='pivotPair'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='trade',
            name='priceClosedShort',
            field=models.CharField(default=1, max_length=255, verbose_name='priceClosedShort'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='trade',
            name='priceEnteredShort',
            field=models.CharField(default=1, max_length=255, verbose_name='priceEnteredShort'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='trade',
            name='priceOfA',
            field=models.CharField(default=1, max_length=255, verbose_name='priceOfA'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='trade',
            name='priceOfB',
            field=models.CharField(default=1, max_length=255, verbose_name='priceOfB'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='trade',
            name='rsiOnEnter',
            field=models.CharField(default=1, max_length=255, verbose_name='rsiOnEnter'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='trade',
            name='stockNameFull',
            field=models.CharField(default=1, max_length=255, verbose_name='stockNameFull'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='trade',
            name='stockNameSymbol',
            field=models.CharField(default=1, max_length=255, verbose_name='stockNameSymbol'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='trade',
            name='stopLoss',
            field=models.CharField(default=1, max_length=255, verbose_name='stopLoss'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='trade',
            name='takeProfit',
            field=models.CharField(default=1, max_length=255, verbose_name='takeProfit'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='trade',
            name='tradeCloseDate',
            field=models.CharField(default=1, max_length=255, verbose_name='tradeCloseDate'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='trade',
            name='tradeClosed',
            field=models.CharField(default=11, max_length=255, verbose_name='tradeClosed'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='trade',
            name='tradeDuration',
            field=models.CharField(default=1, max_length=255, verbose_name='tradeDuration'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='trade',
            name='tradeID',
            field=models.CharField(default=1, max_length=255, verbose_name='tradeID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='trade',
            name='tradeOpen',
            field=models.CharField(default=1, max_length=255, verbose_name='tradeOpen'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='trade',
            name='tradeResult',
            field=models.CharField(default=1, max_length=255, verbose_name='tradeResult'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='trade',
            name='tradeStartDate',
            field=models.CharField(default=1, max_length=255, verbose_name='tradeStartDate'),
            preserve_default=False,
        ),
    ]