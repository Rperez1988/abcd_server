# todos/serializers.py
from rest_framework import serializers
from .models import activeTrades, stock, stockStatistics, strategyResults, tradeResults, chartImage, totalResults, stocksTested, savedLists


class StockSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'date',
            'open',
            'close',
            'high',
            'low',
            'adjClose',
            'volume'

        )
        model = stock

class StrategyResultSerializer(serializers.ModelSerializer):

    class Meta:
        fields = (
            'active',
            'stock',
            'length',
            'total_open',
            'total_close',
            'total_won',
            'total_lost',
            'pnl',
            'strike_rate',
            'largestWin',
            'largestLost'
        )
        model = strategyResults

class TradeResultSerializer(serializers.ModelSerializer):

    class Meta:
        fields = (
            'tradeid',
            'stock',
            'trade_result',
            'pnl',
            'date_of_pivot_high',  
            'date_of_pivot_low',
            'date_pivot_high_snr_tested',
            'date_entered_short',
            'date_closed_short',
            'price_of_pivot_high',
            'price_of_pivot_low',
            'price_pivot_high_snr_tested',
            'price_entered_short',
            'price_closed_short',
            'high_close_mark',
            'low_close_mark',
            'rsi',
            'riskRewardRatio',
            'risk',
            'reward'
            # 'image',



            
        )
        model = tradeResults

class ChartImageSerializer(serializers.ModelSerializer):

    class Meta:
        fields = (
            'image',
            

        )
        model = chartImage

class TotalResultsSerializer(serializers.ModelSerializer):

    class Meta:
        fields = (
            'tested',
            'totalOpen', 
            'totalClosed',
            'totalWon', 
            'totalLost',  
            'totalPnl',  
            'totalWr',  
            'largestWin',
            'largestLost',
            'avgWin',
            'avgLost',
            'avgTrade',
            'longestTrade',
            'shortestTrade',
            'longestOneToTwo',
            'shortestOneToTwo',
            'avgOneToTwo',
            'longestTwoToShort',
            'shortestTwoToShort',
            'avgTwoToShort',
        )
        model = totalResults

class StocksTestedSerializer(serializers.ModelSerializer):

    class Meta:
        fields = (
            'stock',
        )

        model = stocksTested

class SavedListsSerializer(serializers.ModelSerializer):

    class Meta:
        fields = (
            'name',
            'stock',
        )

        model = savedLists

class StockStatisticsSerializer(serializers.ModelSerializer):

    class Meta:
        fields = (
            'stock',
            'totalPnl',
            'avgPnl',
            'largestWin',
            'largestLost',
            'avgWin',
            'avgLost',
            'longestTrade',
            'shortestTrade',
            'avgTrade',
        )
        model = stockStatistics

class ActiveTradeSerializer(serializers.ModelSerializer):

    class Meta:
        fields = (
            'tradeid',
            'shares_purchased',
            'date_of_pivot_high',
            'date_of_pivot_low',
            'price_of_pivot_high',
            'price_of_pivot_low',
            'pair_range',
            'days_between_pivots',
            'date_pivot_high_snr_tested',
            'price_pivot_high_snr_tested',
            'date_entered_short',
            'price_entered_short',
            'high_close_mark',
            'low_close_mark',
            'lowest_price_went',
            'highest_price_went',
            'pnl',
            'cash_invested',
            'current_cash_in_hand',
            'trades_active',
            'symbol',
            'activePrice',
            'tradeType',
            'durationOfTrade',
            'ohlc'
    
        )
        model = activeTrades

