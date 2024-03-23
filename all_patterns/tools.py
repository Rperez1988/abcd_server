from rest_framework import generics
from .serializers import *
from .models import *
from rest_framework import generics
from django.http import HttpResponse
from CandleData.models import *
from django.views.decorators.csrf import csrf_exempt
from .tools import *
from django.db import transaction


def create_Selected_ABCD_pattern(pattern_instance):

    selected_instance = Selected_ABCD(
                trade_symbol=pattern_instance.trade_symbol,
                pattern_A_start_date=pattern_instance.pattern_A_start_date,
                pattern_A_pivot_date=pattern_instance.pattern_A_pivot_date,
                pattern_A_end_date=pattern_instance.pattern_A_end_date,
                pattern_A_open=pattern_instance.pattern_A_open,
                pattern_A_high=pattern_instance.pattern_A_high,
                pattern_A_close=pattern_instance.pattern_A_close,
                pattern_A_low=pattern_instance.pattern_A_low,

                pattern_B_start_date=pattern_instance.pattern_B_start_date,
                pattern_B_pivot_date=pattern_instance.pattern_B_pivot_date,
                pattern_B_end_date=pattern_instance.pattern_B_end_date,
                pattern_B_open=pattern_instance.pattern_B_open,
                pattern_B_high=pattern_instance.pattern_B_high,
                pattern_B_close=pattern_instance.pattern_B_close,
                pattern_B_low=pattern_instance.pattern_B_low,

                pattern_C_start_date=pattern_instance.pattern_C_start_date,
                pattern_C_pivot_date=pattern_instance.pattern_C_pivot_date,
                pattern_C_end_date=pattern_instance.pattern_C_end_date,
                pattern_C_open=pattern_instance.pattern_C_open,
                pattern_C_high=pattern_instance.pattern_C_high,
                pattern_C_close=pattern_instance.pattern_C_close,
                pattern_C_low=pattern_instance.pattern_C_low,

                pattern_AB_start_date=pattern_instance.pattern_AB_start_date,
                pattern_AB_end_date=pattern_instance.pattern_AB_end_date,
                pattern_AB_bar_duration=pattern_instance.pattern_AB_bar_duration,

                pattern_ABC_start_date=pattern_instance.pattern_ABC_start_date,
                pattern_ABC_end_date=pattern_instance.pattern_ABC_end_date,
                pattern_ABC_bar_length=pattern_instance.pattern_ABC_bar_length,
                pattern_C_bar_retracement=pattern_instance.pattern_C_bar_retracement,
                pattern_C_price_retracement=pattern_instance.pattern_C_price_retracement,
                pattern_BC_bar_length=pattern_instance.pattern_BC_bar_length,

                pattern_ABCD_bar_length=pattern_instance.pattern_ABCD_bar_length,
                pattern_ABCD_start_date=pattern_instance.pattern_ABCD_start_date,
                pattern_ABCD_end_date=pattern_instance.pattern_ABCD_end_date,
                pattern_D_bar_retracement=pattern_instance.pattern_D_bar_retracement,
                pattern_D_price_retracement=pattern_instance.pattern_D_price_retracement,
                pattern_CD_bar_length=pattern_instance.pattern_CD_bar_length,

                trade_is_open=pattern_instance.trade_is_open,
                trade_is_closed=pattern_instance.trade_is_closed,
                trade_entered_date=pattern_instance.trade_entered_date,
                trade_entered_price=pattern_instance.trade_entered_price,
                trade_exited_date=pattern_instance.trade_exited_date,
                trade_exited_price=pattern_instance.trade_exited_price,
                trade_risk=pattern_instance.trade_risk,
                trade_reward=pattern_instance.trade_reward,
                trade_take_profit=pattern_instance.trade_take_profit,
                trade_stop_loss=pattern_instance.trade_stop_loss,
                
                trade_duration_bars=pattern_instance.trade_duration_bars,
                trade_duration_days=pattern_instance.trade_duration_days,
                trade_pnl=pattern_instance.trade_pnl,
                trade_result=pattern_instance.trade_result,
                trade_return_percentage=pattern_instance.trade_return_percentage,
                trade_rrr=pattern_instance.trade_rrr,
                trade_created=pattern_instance.trade_created,

                current_date = pattern_instance.current_date,

                d_dropped_below_b = pattern_instance.d_dropped_below_b
            )
            
        #     # Save the new instance
    selected_instance.save()


    return

def check_symbols_ran(request):

    all_symbols_from_patterns = list(Pattern_ABCD.objects.values('trade_symbol').distinct())
    all_symbols_from_candles = list(Candle.objects.values('symbol').distinct())

    print('Last Symbol Ran:', all_symbols_from_patterns[-1], len(all_symbols_from_patterns))

    for i,each in enumerate(all_symbols_from_candles):
        if each['symbol'] == all_symbols_from_patterns[-1]['trade_symbol']:
            print("next index:",i)

    


    return HttpResponse('symbols ran')

def getBodyContext(request, str):

    body_unicode = request.body.decode('utf-8')
    
    import ast
    d = ast.literal_eval(body_unicode)
    


    return (d[str])