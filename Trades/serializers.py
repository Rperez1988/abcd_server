from rest_framework import serializers
from .models import *
class TradeSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (

            'trade_id', 
            'symbol',
            'exchange', 
            'trade_start_date',
            'trade_end_date' ,
            'trade_duration' ,
            'trade_open' ,
            'trade_closed',
            'trade_market',
            'trade_result',
            'current_candle_price',
            'current_candle_date',
            # pivot_number
            'lowest_price_dropped' ,
            'current_candle_rsi' ,
            'current_candle_volume' ,
            # average_volume =
            # percentage_change = 


            # PNL
            'risk' ,
            'reward' ,
            'stop_loss' ,
            'take_profit' ,
            'pnl' ,
            'return_percentage' ,
            'risk_reward_ratio' ,


            

        )
        model = Trade

class SinglePivotSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (

     
        'pivot_id', 
        'pivot_letter',
        'pivot_color',
        'pivot_length', 

        'pivot_start_date', 
        'pivot_date', 
        'pivot_end_date', 
        'pivot_open',
        'pivot_high',
        'pivot_close',
        'pivot_low',

        'bars_between_previous_pivot', 
        'days_between_previous_pivot',
    
      


            

        )
        model = Single_A_Pivot
