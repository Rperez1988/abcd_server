from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics
from .serializers import TradeSerializer
from trade.models import all_trades
from django.core.cache import cache

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
    queryset            = all_trades.objects.all()[:20]
    serializer_class    = TradeSerializer

class incrementTradesInView(generics.ListCreateAPIView):
    # serializer_class = TradeSerializer
    queryset            = all_trades.objects.all()[:20]
    serializer_class    = TradeSerializer


    def get_queryset(self):
        # Retrieve the current record_count from the cache or set it to 20 if it doesn't exist
        record_count = cache.get('record_count')
        if record_count is None:
            record_count = 20

        # Update the queryset to fetch 'record_count' number of records
        queryset = all_trades.objects.all()[:record_count]

        # Increment the record_count for the next request and store it in the cache
        record_count += 20
        cache.set('record_count', record_count)

        return queryset
    