from django.shortcuts import render
from .models import *
from rest_framework import generics
from .serializers import *

def createTrades(trade):


    # tradeInfo = trade['tradeInfo'],
    # pivotInfo = trade['pivotInfo'],
    # movement = trade['movement'],
    # settings = trade['settings'],
    # pnl = trade['pnl'],
    # retracement =  trade['retracement'],
    # enterExitInfo = trade['enterExitInfo'],
    # duration = trade['duration'],
    # chartData = trade['chartData'],
    # length = trade['length']


    Trade.objects.update_or_create(

        # TRADE INFO
        symbol = trade['tradeInfo']['symbol'],
        exchange = trade['tradeInfo']['exchange'],
        trade_start_date = trade['tradeInfo']['startDate'],
        trade_end_date = trade['tradeInfo']['endDate'],
        trade_duration = trade['tradeInfo']['tradeDuration'],
        trade_open = trade['tradeInfo']['tradeOpen'],
        trade_closed = trade['tradeInfo']['tradeClosed'],
        # trade_market = trade['tradeInfo']['tradeMarket'],
        trade_result = trade['tradeInfo']['tradeResult'],
        current_candle_price = trade['tradeInfo']['currentPrice'],
        current_candle_date = trade['tradeInfo']['currentDate'],
        lowest_price_dropped = trade['tradeInfo']['lowest_price_dropped'],
        current_candle_rsi = trade['tradeInfo']['rsi'],
        current_candle_volume = trade['tradeInfo']['volume'],

        # PNL
        risk = trade['pnl']['risk'],
        reward = trade['pnl']['reward'],
        stop_loss = trade['pnl']['stopLoss'],
        take_profit = trade['pnl']['takeProfit'],
        pnl = trade['pnl']['pnl'],
        return_percentage = trade['pnl']['returnPercentage'],
        risk_reward_ratio = trade['pnl']['riskRewardRatio'],

        # Enter Exit Info
        

    )


    return

class TradeSerializer(generics.ListCreateAPIView):
    queryset            = Trade.objects.all()
    serializer_class    = TradeSerializer

def delete(request):


    return 

def createPivots(pivot):
    Single_A_Pivot.objects.update_or_create(

        pivot_letter = pivot['pivot_letter'],
        pivot_color =pivot['pivotColor'],
        pivot_length = pivot['full_length'],

        pivot_start_date = pivot['pivotStartDate'],
        pivot_date = pivot['pivotDate'],
        pivot_end_date = pivot['pivotEndDate'],
        pivot_open = pivot['open'],
        pivot_high = pivot['high'],
        pivot_close = pivot['close'],
        pivot_low = pivot['low'],

        bars_between_previous_pivot = pivot['barsSincePreviousPivot'],
        days_between_previous_pivot = pivot['daysSincePreviousPivot'],
        )
    
    return
class SinglePivotSerializer(generics.ListCreateAPIView):
    queryset            = Single_A_Pivot.objects.all()
    serializer_class    = SinglePivotSerializer
