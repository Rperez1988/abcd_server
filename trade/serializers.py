from rest_framework import serializers
from trade.models import all_trades


class TradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = all_trades
        fields = '__all__'
        # fields = (
            
        #     'settingsName',
        #     'tradeID',
        #     'exchange',
        #     # 'stockNameFull' ,
        #     'stockNameSymbol',
        #     'currentPrice' ,
        #     'currentDate',
        #     'tradeDuration' ,
        #     'tradeOpen',
        #     'tradeClosed',
        #     'closingTradeType',
        #     'completeTradeType',
        #     'openingTradeType',
        #     'tradeResult',
        #     'pnl' ,
        #     'riskRewardRatio',
        #     'rsi',
        #     'rsiOnEnter',
        #     'risk',
        #     'reward',
        #     'pivotPair',
        #     'dateOfA',
        #     'dateOfB',
        #     'dateOfC' ,
        #     'dateOfD' ,
        #     'priceOfA',
        #     'priceOfB',
        #     'priceOfC',
        #     'priceOfD',
        #     'stopLoss' ,
        #     'takeProfit',
        #     'chartData',
        #     'tradeStartDate',
        #     'tradeCloseDate',
        #     'daysSinceStartDate',
        #     'length_AtoB',
        #     'length_BtoC',
        #     'length_CtoD',
        #     'length_AtoD',
        #     'furthestOfA',
        #     'bcRetracement',
        #     'returnPercentage',
        #     'settings'
           
            
            
            


        # )
        # model = trade
