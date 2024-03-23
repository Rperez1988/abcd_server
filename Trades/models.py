from django.db import models
import uuid
from django.utils import timezone
class Trade(models.Model):

    # TRADE INFO
    trade_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    # abc_id=
    symbol = models.CharField(max_length=100,default=None, null=True, blank=True)
    exchange = models.CharField(max_length=100,default=None, null=True, blank=True)
    trade_start_date = models.DateField(default=None, null=True, blank=True)
    trade_end_date = models.DateField(default=None, null=True, blank=True)
    trade_duration = models.IntegerField(default=None, null=True, blank=True)
    trade_open = models.BooleanField(default=None, null=True, blank=True)
    trade_closed = models.BooleanField()
    trade_market = models.CharField(max_length=100,default=None, null=True, blank=True)
    trade_result = models.CharField(max_length=100,default=None, null=True, blank=True)
    current_candle_price = models.FloatField(default=None, null=True, blank=True)
    current_candle_date = models.DateField(default=None, null=True, blank=True)
    # pivot_number
    lowest_price_dropped = models.FloatField(default=None, null=True, blank=True)
    current_candle_rsi = models.FloatField(default=None, null=True, blank=True)
    current_candle_volume = models.FloatField(default=None, null=True, blank=True)
    # average_volume =
    # percentage_change = 


    # PNL
    risk = models.FloatField(default=None, null=True, blank=True)
    reward = models.FloatField(default=None, null=True, blank=True)
    stop_loss = models.FloatField(default=None, null=True, blank=True)
    take_profit = models.FloatField(default=None, null=True, blank=True)
    pnl = models.FloatField(default=None, null=True, blank=True)
    return_percentage = models.FloatField(default=None, null=True, blank=True)
    risk_reward_ratio = models.IntegerField(default=None, null=True, blank=True)


    # Enter Exit Info
    enter_price = models.FloatField(default=None, null=True, blank=True)
    enter_date = models.DateField(default=None, null=True, blank=True)
    exit_price = models.FloatField(default=None, null=True, blank=True)
    exit_date = models.FloatField(default=None, null=True, blank=True)

    # Duration
    a_to_b_length_bars = models.IntegerField(default=None, null=True, blank=True)
    b_to_c_length_bars = models.IntegerField(default=None, null=True, blank=True)
    c_to_d_length_bars = models.IntegerField(default=None, null=True, blank=True)
    a_to_b_length_days = models.IntegerField(default=None, null=True, blank=True)
    b_to_c_length_days = models.IntegerField(default=None, null=True, blank=True)
    c_to_d_length_days = models.IntegerField(default=None, null=True, blank=True)

    # Retracement
    bc_retracement = models.FloatField(default=None, null=True, blank=True)
    cd_retracement = models.FloatField(default=None, null=True, blank=True)





class Single_A_Pivot(models.Model):

    pivot_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    pivot_letter = models.CharField(max_length=100)
    pivot_color = models.CharField(max_length=100)
    pivot_length = models.IntegerField()

    pivot_start_date = models.DateField()
    pivot_date = models.DateField()
    pivot_end_date = models.DateField()
    pivot_open = models.FloatField()
    pivot_high = models.FloatField()
    pivot_close = models.FloatField()
    pivot_low = models.FloatField()

    bars_between_previous_pivot = models.IntegerField()
    days_between_previous_pivot = models.IntegerField()
    

