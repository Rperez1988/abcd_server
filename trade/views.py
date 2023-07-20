from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics
from .serializers import TradeSerializer
from trade.models import all_trades

def createTrade(trade_):

    all_trades.objects.get_or_create(

        tradeInfo = trade_['tradeInfo'],
        pivotInfo = trade_['pivotInfo'],
        movement = trade_['movement'],
        settings = trade_['settings'],
        pnl = trade_['pnl'],
        retracement =  trade_['retracement'],
        enterExitInfo = trade_['enterExitInfo'],
        duration = trade_['duration'],
        chartData = trade_['chartData'],
        length = trade_['length']
    )

    return

class tradeModels(generics.ListCreateAPIView):
    queryset            = all_trades.objects.all()
    serializer_class    = TradeSerializer
