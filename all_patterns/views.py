from rest_framework import generics
from .serializers import *
from .models import *
from rest_framework import generics
from django.http import HttpResponse
from CandleData.models import *
from django.views.decorators.csrf import csrf_exempt
from .tools import *
from django.db import transaction

from uuid import UUID

def create_patterns_models(abcd, abc, ab, a):

    # CREATE A PATTERNS
    for each in a:

        try: 
            Pattern_A.objects.update_or_create(
                trade_symbol = each.trade_symbol,
                pattern_A_start_date =each.pattern_A_start_date,
                pattern_A_pivot_date = each.pattern_A_pivot_date,
                pattern_A_end_date = each.pattern_A_end_date,
                pattern_A_open = each.pattern_A_open,
                pattern_A_high = each.pattern_A_high,
                pattern_A_close = each.pattern_A_close,
                pattern_A_low = each.pattern_A_low,
                pattern_AB_bar_duration = each.pattern_AB_bar_duration,
            )
        except Exception as e:
            print(f'pattern A {e}')
    
    # CREATE AB PATTERNS
    for each in ab:
       
        try:
            Pattern_AB.objects.update_or_create(

                trade_symbol = each.trade_symbol,
                pattern_BC_bar_duration = each.pattern_AB_bar_duration,
                pattern_A_start_date =each.pattern_A_start_date,
                pattern_A_pivot_date = each.pattern_A_pivot_date,
                pattern_A_end_date = each.pattern_A_end_date,
                pattern_A_open = each.pattern_A_open,
                pattern_A_high = each.pattern_A_high,
                pattern_A_close = each.pattern_A_close,
                pattern_A_low = each.pattern_A_low,

                # PATTERN B
                pattern_B_start_date =each.pattern_B_start_date,
                pattern_B_pivot_date = each.pattern_B_pivot_date,
                pattern_B_end_date = each.pattern_B_end_date,
                pattern_B_open = each.pattern_B_open,
                pattern_B_high = each.pattern_B_high,
                pattern_B_close = each.pattern_B_close,
                pattern_B_low = each.pattern_B_low,

                # PATTERN AB
                pattern_AB_start_date = each.pattern_B_start_date,
                pattern_AB_end_date = each.pattern_B_end_date,
                pattern_AB_bar_duration = each.pattern_AB_bar_duration,
                
            )
        except Exception as e:
            print(f'Pattern_AB {e}')
    
    # CREATE ABC PATTERNS
    for each in abc:
      
        try:
            Pattern_ABC.objects.update_or_create(

                trade_symbol = each.trade_symbol,
         
                # PATTERN A
                pattern_A_start_date = each.pattern_A_start_date,
                pattern_A_pivot_date = each.pattern_A_pivot_date,
                pattern_A_end_date = each.pattern_A_end_date,
                pattern_A_open = each.pattern_A_open,
                pattern_A_high = each.pattern_A_high,
                pattern_A_close = each.pattern_A_close,
                pattern_A_low = each.pattern_A_low,

                # PATTERN B
                pattern_B_start_date = each.pattern_B_start_date,
                pattern_B_pivot_date = each.pattern_B_pivot_date,
                pattern_B_end_date = each.pattern_B_end_date,
                pattern_B_open = each.pattern_B_open,
                pattern_B_high = each.pattern_B_high,
                pattern_B_close = each.pattern_B_close,
                pattern_B_low = each.pattern_B_low,

                # Pattern C
                pattern_C_start_date = each.pattern_C_start_date,
                pattern_C_pivot_date = each.pattern_C_pivot_date,
                pattern_C_end_date = each.pattern_C_end_date,
                pattern_C_open =each.pattern_C_open,
                pattern_C_high =each.pattern_C_high,
                pattern_C_close =each.pattern_C_close,
                pattern_C_low =each.pattern_C_low,

                # PATTERN AB
                pattern_AB_start_date = each.pattern_AB_start_date,
                pattern_AB_end_date =each.pattern_AB_end_date,
                pattern_AB_bar_length = each.pattern_AB_bar_length,

                # PATTERN ABC
                pattern_ABC_start_date = each.pattern_ABC_start_date,
                pattern_ABC_end_date = each.pattern_ABC_end_date,
                pattern_ABC_bar_length = each.pattern_ABC_bar_length,
                pattern_C_bar_retracement = each.pattern_C_bar_retracement,
                pattern_C_price_retracement = each.pattern_C_price_retracement,
                pattern_BC_bar_length = each.pattern_BC_bar_length,
                pattern_ABC_found_D = each.pattern_ABC_found_D,

            )
        except Exception as e:
    
            print(f'Pattern_ABC {e}')
    
    # CREATE ABCD PATTERNS
    for each in abcd:
        
        print('=========================')
        pattern_exists = Pattern_ABCD.objects.filter(
            trade_symbol=each.trade_symbol,
            pattern_A_pivot_date=each.pattern_A_pivot_date,
            pattern_B_pivot_date=each.pattern_B_pivot_date,
            pattern_C_pivot_date=each.pattern_C_pivot_date,
            pattern_ABCD_end_date=each.pattern_ABCD_end_date
        
            ).exists()

        if pattern_exists:
            print("Pattern exists.")
        else:
            # print("Pattern does not exist.")
      
            try:
                pattern = Pattern_ABCD.objects.create(

                    trade_symbol = each.trade_symbol,

                    # PATTERN A
                    # pattern_A_id = 'hello world',
                    pattern_A_start_date = each.pattern_A_start_date,
                    pattern_A_pivot_date = each.pattern_A_pivot_date,
                    pattern_A_end_date = each.pattern_A_end_date,
                    pattern_A_open = each.pattern_A_open,
                    pattern_A_high = each.pattern_A_high,
                    pattern_A_close = each.pattern_A_close,
                    pattern_A_low = each.pattern_A_low,

                    # PATTERN B
                    pattern_B_start_date = each.pattern_B_start_date,
                    pattern_B_pivot_date = each.pattern_B_pivot_date,
                    pattern_B_end_date = each.pattern_B_end_date,
                    pattern_B_open = each.pattern_B_open,
                    pattern_B_high = each.pattern_B_high,
                    pattern_B_close = each.pattern_B_close,
                    pattern_B_low = each.pattern_B_low,

                    # Pattern C
                    pattern_C_start_date = each.pattern_C_start_date,
                    pattern_C_pivot_date = each.pattern_C_pivot_date,
                    pattern_C_end_date = each.pattern_C_end_date,
                    pattern_C_open = each.pattern_C_open,
                    pattern_C_high = each.pattern_C_high,
                    pattern_C_close = each.pattern_C_close,
                    pattern_C_low = each.pattern_C_low,

                    # PATTERN AB
                    pattern_AB_start_date = each.pattern_AB_start_date,
                    pattern_AB_end_date =each.pattern_AB_end_date,
                    pattern_AB_bar_duration = each.pattern_AB_bar_length,
        
                    # PATTERN ABC
                    pattern_ABC_start_date = each.pattern_ABC_start_date,
                    pattern_ABC_end_date = each.pattern_ABC_end_date,
                    pattern_ABC_bar_length = each.pattern_ABC_bar_length,
                    pattern_C_bar_retracement = each.pattern_C_bar_retracement,
                    pattern_C_price_retracement = each.pattern_C_price_retracement,
                    pattern_BC_bar_length = each.pattern_BC_bar_length,


                    # PATTERN ABCD
                    pattern_ABCD_bar_length = each.pattern_ABCD_bar_length,
                    pattern_ABCD_start_date = each.pattern_ABCD_start_date,
                    pattern_ABCD_end_date = each.pattern_ABCD_end_date,
                    pattern_D_bar_retracement = each.pattern_D_bar_retracement,
                    pattern_D_price_retracement = each.pattern_D_price_retracement,
                    pattern_CD_bar_length = each.pattern_CD_bar_length,

                    # Trade
                    trade_is_open = each.trade_is_open,
                    trade_is_closed =each.trade_is_closed,
                    trade_entered_date = each.trade_entered_date,
                    trade_entered_price = each.trade_entered_price,
                    trade_exited_date = each.trade_exited_date,
                    trade_exited_price = each.trade_exited_price,
                    trade_risk = each.trade_risk,
                    trade_reward = each.trade_reward,
                    trade_take_profit = each.trade_take_profit,
                    trade_stop_loss =each.trade_stop_loss,
                    trade_duration_bars =  each.trade_duration_bars,
                    trade_duration_days =  each.trade_duration_days,
                    trade_pnl =each.trade_pnl,
                    trade_result =each.trade_result,
                    trade_return_percentage =each.trade_return_percentage,
                    trade_rrr = each.trade_rrr,
                    trade_created = each.trade_created,

                    current_date = each.current_date,

                    d_dropped_below_b = each.d_dropped_below_b, 

                    candle_ids = [';']
            
                )
                
                
                objects_list = []

                candle_uuids = [UUID(uuid_str) for uuid_str in each.trade_candle_ids]
                
                candles_queryset = Candle.objects.filter(candle_id__in=candle_uuids).order_by('candle_date')
                print(list(candles_queryset)[0])
               
                if candles_queryset.exists():

                    objects_list = list(candles_queryset)
               
                    pattern.candles.set(objects_list)

            except Exception as e:
                print(f'Pattern_ABCD Error: {e}')
   
    return HttpResponse('CREATE PATTERNS') 



def selected_patterns(selected_patterns):

    Selected_ABCD.objects.all().delete()

    pattern_instances = Pattern_ABCD.objects.filter(id__in=selected_patterns)[:1000]

    # Create Selected_ABCD instances based on Pattern_ABCD instances
    for pattern_instance in pattern_instances:
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
        
        # Save the new instance
        selected_instance.save()


@csrf_exempt
def sort_selected(request):

    Selected_ABCD.objects.all().delete()

    # pattern_instances = Pattern_ABCD.objects.filter(trade_entered_price__lt=1).order_by('trade_duration_bars','trade_entered_price')[:500]

    # Create Selected_ABCD instances based on Pattern_ABCD instances
    

    sort_by = getBodyContext(request,'sort')
 
    sort_filter = None

    if sort_by == 'DURATION':
        sort_filter = 'trade_duration_bars'
    elif sort_by == 'PNL':
        sort_filter = 'trade_pnl'

    Selected_ABCD.objects.all().delete()
    pattern_instances = Pattern_ABCD.objects.all().order_by(sort_filter)[:100]
    for pattern_instance in pattern_instances:
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
        
        # Save the new instance
        selected_instance.save()


    


    return HttpResponse('sort')

def delete_all_patterns(request):

    Pattern_ABCD.objects.all().delete()

    return HttpResponse('Delete all patterns')

@csrf_exempt
def update_patterns_list_count(request):

    count = getBodyContext(request, 'count')

    count = 100 * count
    with transaction.atomic():

        Selected_ABCD.objects.all().delete()

        pattern_instances = Pattern_ABCD.objects.all()[:count]

        for pattern_instance in pattern_instances:
            create_Selected_ABCD_pattern(pattern_instance)

            

    return HttpResponse('update')



class A_Patterns_Serializer(generics.ListCreateAPIView):
    queryset            = Pattern_A.objects.all()
    serializer_class    = Pattern_A_Serializer

class AB_Patterns_Serializer(generics.ListCreateAPIView):
    queryset            = Pattern_AB.objects.all()
    serializer_class    = Pattern_AB_Serializer

class ABC_Patterns_Serializer(generics.ListCreateAPIView):
    queryset            = Pattern_ABC.objects.all()
    serializer_class    = Pattern_ABC_Serializer

class Patterns_Serializer(generics.ListCreateAPIView):
    queryset            = Pattern_ABCD.objects.all()
    serializer_class    = Pattern_ABCD_Serializer

class Selected_ABCD_Serializer(generics.ListCreateAPIView):
    queryset            = Selected_ABCD.objects.all()
    serializer_class    = Selected_ABCD_Serializer