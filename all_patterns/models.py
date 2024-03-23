from django.db import models

from CandleData.models import Candle
import uuid


from django.db import models

class Pattern_A(models.Model):
    trade_symbol = models.CharField(max_length=100, null=True)
    pattern_A_start_date = models.DateField(null=True)
    pattern_A_pivot_date = models.DateField(null=True)
    pattern_A_end_date = models.DateField(null=True)
    pattern_A_open = models.DecimalField(null=True, max_digits=6, decimal_places=2)
    pattern_A_high = models.DecimalField(null=True, max_digits=6, decimal_places=2)
    pattern_A_close = models.DecimalField(null=True, max_digits=6, decimal_places=2)
    pattern_A_low = models.DecimalField(null=True, max_digits=6, decimal_places=2)
    pattern_AB_bar_duration = models.IntegerField(null=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=[
                    'trade_symbol',
                    'pattern_A_start_date',
                    'pattern_A_pivot_date',
                    'pattern_A_end_date',
                    'pattern_A_open',
                    'pattern_A_high',
                    'pattern_A_close',
                    'pattern_A_low',
                    'pattern_AB_bar_duration',
                ],
                name='unique_pattern_a'
            )
        ]

class Pattern_AB(models.Model):
    trade_symbol = models.CharField(max_length=100, null=True)
    pattern_BC_bar_duration = models.IntegerField(null=True)
    pattern_A_start_date = models.DateField(null=True)
    pattern_A_pivot_date = models.DateField(null=True)
    pattern_A_end_date = models.DateField(null=True)
    pattern_A_open = models.DecimalField(null=True, max_digits=6, decimal_places=2)
    pattern_A_high = models.DecimalField(null=True, max_digits=6, decimal_places=2)
    pattern_A_close = models.DecimalField(null=True, max_digits=6, decimal_places=2)
    pattern_A_low = models.DecimalField(null=True, max_digits=6, decimal_places=2)
    pattern_B_start_date = models.DateField(null=True)
    pattern_B_pivot_date = models.DateField(null=True)
    pattern_B_end_date = models.DateField(null=True)
    pattern_B_open = models.DecimalField(null=True, max_digits=6, decimal_places=2)
    pattern_B_high = models.DecimalField(null=True, max_digits=6, decimal_places=2)
    pattern_B_close = models.DecimalField(null=True, max_digits=6, decimal_places=2)
    pattern_B_low = models.DecimalField(null=True, max_digits=6, decimal_places=2)
    pattern_AB_start_date = models.DateField(null=True)
    pattern_AB_end_date = models.DateField(null=True)
    pattern_AB_bar_duration = models.IntegerField(null=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=[
                    'trade_symbol',
                  
                    'pattern_A_pivot_date',
                  
                    'pattern_B_start_date',
                    'pattern_B_pivot_date',
                    'pattern_B_end_date',
                    'pattern_B_open',
                    'pattern_B_high',
                    'pattern_B_close',
                    'pattern_B_low',
                    'pattern_AB_start_date',
                    'pattern_AB_end_date',
                    'pattern_AB_bar_duration',
                ],
                name='unique_pattern_ab'
            )
        ]

class Pattern_ABC(models.Model):
    trade_symbol = models.CharField(max_length=100, null=True)

    pattern_A_start_date = models.DateField(null=True)
    pattern_A_pivot_date = models.DateField(null=True)
    pattern_A_end_date = models.DateField(null=True)
    pattern_A_open = models.DecimalField(null=True, max_digits=6, decimal_places=2)
    pattern_A_high = models.DecimalField(null=True, max_digits=6, decimal_places=2)
    pattern_A_close = models.DecimalField(null=True, max_digits=6, decimal_places=2)
    pattern_A_low = models.DecimalField(null=True, max_digits=6, decimal_places=2)

    pattern_B_start_date = models.DateField(null=True)
    pattern_B_pivot_date = models.DateField(null=True)
    pattern_B_end_date = models.DateField(null=True)
    pattern_B_open = models.DecimalField(null=True, max_digits=6, decimal_places=2)
    pattern_B_high = models.DecimalField(null=True, max_digits=6, decimal_places=2)
    pattern_B_close = models.DecimalField(null=True, max_digits=6, decimal_places=2)
    pattern_B_low = models.DecimalField(null=True, max_digits=6, decimal_places=2)

    pattern_C_start_date = models.DateField(null=True)
    pattern_C_pivot_date = models.DateField(null=True)
    pattern_C_end_date = models.DateField(null=True)
    pattern_C_open = models.DecimalField(null=True, max_digits=6, decimal_places=2)
    pattern_C_high = models.DecimalField(null=True, max_digits=6, decimal_places=2)
    pattern_C_close = models.DecimalField(null=True, max_digits=6, decimal_places=2)
    pattern_C_low = models.DecimalField(null=True, max_digits=6, decimal_places=2)

    pattern_AB_start_date = models.DateField(null=True)
    pattern_AB_end_date = models.DateField(null=True)
    pattern_AB_bar_length = models.IntegerField(null=True)
    
    pattern_ABC_start_date = models.DateField(null=True)
    pattern_ABC_end_date = models.DateField(null=True)
    pattern_ABC_bar_length = models.IntegerField(null=True)
    pattern_C_bar_retracement = models.DecimalField(null=True, max_digits=6, decimal_places=2)
    pattern_C_price_retracement = models.DecimalField(null=True, max_digits=6, decimal_places=2)
    pattern_BC_bar_length = models.IntegerField(null=True)
    pattern_ABC_found_D = models.BooleanField(null=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=[
                    'trade_symbol',
                    'pattern_A_pivot_date',

                    'pattern_B_pivot_date',
                 
                    'pattern_C_pivot_date',
        
                    'pattern_AB_start_date',
                    'pattern_AB_end_date',
                    'pattern_AB_bar_length',
                    'pattern_ABC_start_date',
                    'pattern_ABC_end_date',
                    'pattern_ABC_bar_length',
                    'pattern_C_bar_retracement',
                    'pattern_C_price_retracement',
                    'pattern_BC_bar_length',
                ],
                name='unique_pattern_abc'
            )
        ]

from django.db import models

class Pattern_ABCD(models.Model):
    # Trade Symbol
    trade_symbol = models.CharField(max_length=100, null=True)

    # Pattern A
    pattern_A_start_date = models.DateField(null=True)
    pattern_A_pivot_date = models.DateField(null=True)
    pattern_A_end_date = models.DateField(null=True)
    pattern_A_open = models.DecimalField(null=True, max_digits=6, decimal_places=2)
    pattern_A_high = models.DecimalField(null=True, max_digits=6, decimal_places=2)
    pattern_A_close = models.DecimalField(null=True, max_digits=6, decimal_places=2)
    pattern_A_low = models.DecimalField(null=True, max_digits=6, decimal_places=2)

    # Pattern B
    pattern_B_start_date = models.DateField(null=True)
    pattern_B_pivot_date = models.DateField(null=True)
    pattern_B_end_date = models.DateField(null=True)
    pattern_B_open = models.DecimalField(null=True, max_digits=6, decimal_places=2)
    pattern_B_high = models.DecimalField(null=True, max_digits=6, decimal_places=2)
    pattern_B_close = models.DecimalField(null=True, max_digits=6, decimal_places=2)
    pattern_B_low = models.DecimalField(null=True, max_digits=6, decimal_places=2)

    # Pattern C
    pattern_C_start_date = models.DateField(null=True)
    pattern_C_pivot_date = models.DateField(null=True)
    pattern_C_end_date = models.DateField(null=True)
    pattern_C_open = models.DecimalField(null=True, max_digits=6, decimal_places=2)
    pattern_C_high = models.DecimalField(null=True, max_digits=6, decimal_places=2)
    pattern_C_close = models.DecimalField(null=True, max_digits=6, decimal_places=2)
    pattern_C_low = models.DecimalField(null=True, max_digits=6, decimal_places=2)

    # Pattern AB
    pattern_AB_start_date = models.DateField(null=True)
    pattern_AB_end_date = models.DateField(null=True)
    pattern_AB_bar_duration = models.IntegerField(null=True)

    # Pattern ABC
    pattern_ABC_start_date = models.DateField(null=True)
    pattern_ABC_end_date = models.DateField(null=True)
    pattern_ABC_bar_length = models.IntegerField(null=True)
    pattern_C_bar_retracement = models.DecimalField(null=True, max_digits=6, decimal_places=2)
    pattern_C_price_retracement = models.DecimalField(null=True, max_digits=6, decimal_places=2)
    pattern_BC_bar_length = models.IntegerField(null=True)

    # PATTERN ABCD
    pattern_ABCD_bar_length = models.IntegerField(null=True)
    pattern_ABCD_start_date = models.DateField(null=True)
    pattern_ABCD_end_date = models.DateField(null=True)
    pattern_D_bar_retracement = models.DecimalField(null=True, max_digits=6, decimal_places=2)
    pattern_D_price_retracement = models.DecimalField(null=True, max_digits=6, decimal_places=2)
    pattern_CD_bar_length = models.DecimalField(null=True, max_digits=6, decimal_places=2)

    # Trade
    trade_is_open = models.BooleanField(null=True)
    trade_is_closed = models.BooleanField(null=True)
    trade_entered_date = models.DateField(null=True)
    trade_entered_price = models.DecimalField(null=True, max_digits=6, decimal_places=2)
    trade_exited_date = models.DateField(null=True)
    trade_exited_price = models.DecimalField(null=True, max_digits=6, decimal_places=2)
    trade_risk = models.DecimalField(null=True, max_digits=6, decimal_places=2)
    trade_reward = models.DecimalField(null=True, max_digits=6, decimal_places=2)
    trade_take_profit = models.DecimalField(null=True, max_digits=6, decimal_places=2)
    trade_stop_loss = models.DecimalField(null=True, max_digits=6, decimal_places=2)
    
    trade_duration_bars = models.IntegerField(null=True)
    trade_duration_days = models.IntegerField(null=True)
    trade_pnl = models.DecimalField(null=True, max_digits=6, decimal_places=2)
    trade_result = models.CharField(max_length=100, null=True)
    trade_return_percentage = models.DecimalField(null=True, max_digits=6, decimal_places=2)
    trade_rrr = models.DecimalField(null=True, max_digits=6, decimal_places=2)
    trade_created = models.BooleanField(null=True)

    current_date = models.DateField(null=True)

    d_dropped_below_b = models.DateField(null=True)
    candle_ids = models.JSONField()
    candles = models.ManyToManyField(Candle)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=[
                    'trade_symbol',

                    'pattern_A_pivot_date',
                    'pattern_B_pivot_date',
                    'pattern_C_pivot_date',
                    'pattern_C_price_retracement',
               
                    'pattern_ABCD_bar_length',
                    'pattern_ABCD_start_date',
                    'pattern_ABCD_end_date',
                    'pattern_D_price_retracement',
                    'trade_is_open',

                    'trade_is_closed',
                    'trade_entered_date',
                    'trade_entered_price',
                    'trade_exited_date',
                    'trade_exited_price',
                  
                    'trade_result',
            
                ],
                name='unique_pattern_abcd'
            )
        ]

class Selected_ABCD(models.Model):
    # Trade Symbol
    trade_symbol = models.CharField(max_length=100, null=True)

    # Pattern A
    pattern_A_start_date = models.DateField(null=True)
    pattern_A_pivot_date = models.DateField(null=True)
    pattern_A_end_date = models.DateField(null=True)
    pattern_A_open = models.DecimalField(null=True, max_digits=6, decimal_places=2)
    pattern_A_high = models.DecimalField(null=True, max_digits=6, decimal_places=2)
    pattern_A_close = models.DecimalField(null=True, max_digits=6, decimal_places=2)
    pattern_A_low = models.DecimalField(null=True, max_digits=6, decimal_places=2)

    # Pattern B
    pattern_B_start_date = models.DateField(null=True)
    pattern_B_pivot_date = models.DateField(null=True)
    pattern_B_end_date = models.DateField(null=True)
    pattern_B_open = models.DecimalField(null=True, max_digits=6, decimal_places=2)
    pattern_B_high = models.DecimalField(null=True, max_digits=6, decimal_places=2)
    pattern_B_close = models.DecimalField(null=True, max_digits=6, decimal_places=2)
    pattern_B_low = models.DecimalField(null=True, max_digits=6, decimal_places=2)

    # Pattern C
    pattern_C_start_date = models.DateField(null=True)
    pattern_C_pivot_date = models.DateField(null=True)
    pattern_C_end_date = models.DateField(null=True)
    pattern_C_open = models.DecimalField(null=True, max_digits=6, decimal_places=2)
    pattern_C_high = models.DecimalField(null=True, max_digits=6, decimal_places=2)
    pattern_C_close = models.DecimalField(null=True, max_digits=6, decimal_places=2)
    pattern_C_low = models.DecimalField(null=True, max_digits=6, decimal_places=2)

    # Pattern AB
    pattern_AB_start_date = models.DateField(null=True)
    pattern_AB_end_date = models.DateField(null=True)
    pattern_AB_bar_duration = models.IntegerField(null=True)

    # Pattern ABC
    pattern_ABC_start_date = models.DateField(null=True)
    pattern_ABC_end_date = models.DateField(null=True)
    pattern_ABC_bar_length = models.IntegerField(null=True)
    pattern_C_bar_retracement = models.DecimalField(null=True, max_digits=6, decimal_places=2)
    pattern_C_price_retracement = models.DecimalField(null=True, max_digits=6, decimal_places=2)
    pattern_BC_bar_length = models.IntegerField(null=True)

    # PATTERN ABCD
    pattern_ABCD_bar_length = models.IntegerField(null=True)
    pattern_ABCD_start_date = models.DateField(null=True)
    pattern_ABCD_end_date = models.DateField(null=True)
    pattern_D_bar_retracement = models.DecimalField(null=True, max_digits=6, decimal_places=2)
    pattern_D_price_retracement = models.DecimalField(null=True, max_digits=6, decimal_places=2)
    pattern_CD_bar_length = models.DecimalField(null=True, max_digits=6, decimal_places=2)

    # Trade
    trade_is_open = models.BooleanField(null=True)
    trade_is_closed = models.BooleanField(null=True)
    trade_entered_date = models.DateField(null=True)
    trade_entered_price = models.DecimalField(null=True, max_digits=6, decimal_places=2)
    trade_exited_date = models.DateField(null=True)
    trade_exited_price = models.DecimalField(null=True, max_digits=6, decimal_places=2)
    trade_risk = models.DecimalField(null=True, max_digits=6, decimal_places=2)
    trade_reward = models.DecimalField(null=True, max_digits=6, decimal_places=2)
    trade_take_profit = models.DecimalField(null=True, max_digits=6, decimal_places=2)
    trade_stop_loss = models.DecimalField(null=True, max_digits=6, decimal_places=2)
    
    trade_duration_bars = models.IntegerField(null=True)
    trade_duration_days = models.IntegerField(null=True)
    trade_pnl = models.DecimalField(null=True, max_digits=6, decimal_places=2)
    trade_result = models.CharField(max_length=100, null=True)
    trade_return_percentage = models.DecimalField(null=True, max_digits=6, decimal_places=2)
    trade_rrr = models.DecimalField(null=True, max_digits=6, decimal_places=2)
    trade_created = models.BooleanField(null=True)

    current_date = models.DateField(null=True)
    d_dropped_below_b = models.DateField(null=True)
    
    class Meta:

        constraints = [
            models.UniqueConstraint(
                fields=[
                    'trade_symbol',
                    'pattern_A_pivot_date',
                    'pattern_B_pivot_date',
                    'pattern_C_pivot_date',
                    'pattern_C_price_retracement',
               
                    'pattern_ABCD_bar_length',
                    'pattern_ABCD_start_date',
                    'pattern_ABCD_end_date',
                    'pattern_D_price_retracement',
                    'trade_is_open',

                    'trade_is_closed',
                    'trade_entered_date',
                    'trade_entered_price',
                    'trade_exited_date',
                    'trade_exited_price',
                  
                    'trade_result',
            
                ],
                name='unique_selected_abcd'
            )
        ]


class PatternAndCandles(models.Model):

    pattern = models.ForeignKey(Pattern_ABCD, on_delete=models.CASCADE)
    candle = models.ForeignKey(Candle,  on_delete=models.CASCADE)


