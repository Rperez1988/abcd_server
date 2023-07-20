from rest_framework import serializers
from .models import statistics

class StatisticsSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (

            # Trades
            'nasdaqTotalCount', 
            'forexTotalCount', 
            'cryptoTotalCount',
            'optionsTotalCount', 

            'nasdaqClosedCount', 
            'forexClosedCount', 
            'cryptoClosedCount', 
            'optionsClosedCount', 

            'nasdaqActiveCount',
            'forexActiveCount', 
            'cryptoActiveCount', 
            'optionsActiveCount', 

            'totalTradesCount',
            'activeTradesCount', 
            'closedTradesCount',

            # Peformance
            'activePnl',
            'activeWr',
            'activeWinningCount',
            'activeLosingCount',

            'closedPnl',
            'closedWr',
            'closedWinCount',
            'closedLostCount',

            'totalPnl', 
            'totalWr', 
            'totalWinCount',
            'totalLostCount', 
            'totalAvgReturn',

            'longStartPnlTotal',
            'longStartWrTotal',
            'longStartWinsCountTotal',
            'longStartLostCountTotal',
            'longStartCountTotal',

            'shortStartPnlTotal', 
            'shortStartWrTotal',
            'shortStartWinsCountTotal',
            'shortStartLostCountTotal', 
            'shortStartCountTotal', 

            'longEndPnlTotal',
            'longEndWrTotal', 
            'longEndWinsTotal', 
            'longEndLostTotal', 
            'longEndCountTotal', 

            'shortEndPnlTotal',
            'shortEndWrTotal', 
            'shortEndWinsCountTotal', 
            'shortEndLostCountTotal',
            'shortEndCountTotal', 

            'longToShortPnlTotal', 
            'longToShortWrTotal', 
            'longToShortWinCountTotal', 
            'longToShortLostCountTotal',
            'longToShortCountTotal',

            'longToLongPnlTotal',
            'longToLongWrTotal',
            'longToLongWinCountTotal', 
            'longToLongLostCountTotal',
            'longToLongCountTotal', 

            'shortToLongPnlTotal',
            'shortToLongWrTotal',
            'shortToLongWinCountTotal', 
            'shortToLongLostCountTotal', 
            'shortToLongCountTotal', 

            'shortToShortPnlTotal', 
            'shortToShortWrTotal',
            'shortToShortWinCountTotal', 
            'shortToShortLostCountTotal', 
            'shortToShortCountTotal', 

            'longStartPnlClosed',
            'longStartWrClosed',
            'longStartWinsCountClosed',
            'longStartLostCountClosed',
            'longStartCountClosed',

            'shortStartPnlClosed', 
            'shortStartWrClosed',
            'shortStartWinsCountClosed',
            'shortStartLostCountClosed', 
            'shortStartCountClosed', 

            'longEndPnlClosed',
            'longEndWrClosed', 
            'longEndWinsClosed', 
            'longEndLostClosed', 
            'longEndCountClosed', 

            'shortEndPnlClosed',
            'shortEndWrClosed', 
            'shortEndWinsCountClosed', 
            'shortEndLostCountClosed',
            'shortEndCountClosed', 

            'longToShortPnlClosed', 
            'longToShortWrClosed', 
            'longToShortWinCountClosed', 
            'longToShortLostCountClosed',
            'longToShortCountClosed',

            'longToLongPnlClosed',
            'longToLongWrClosed',
            'longToLongWinCountClosed', 
            'longToLongLostCountClosed',
            'longToLongCountClosed', 

            'shortToLongPnlClosed',
            'shortToLongWrClosed',
            'shortToLongWinCountClosed', 
            'shortToLongLostCountClosed', 
            'shortToLongCountClosed', 

            'shortToShortPnlClosed', 
            'shortToShortWrClosed',
            'shortToShortWinCountClosed', 
            'shortToShortLostCountClosed', 
            'shortToShortCountClosed', 


            'longStartPnlActive',
            'longStartWrActive',
            'longStartWinsCountActive',
            'longStartLostCountActive',
            'longStartCountActive',

            'shortStartPnlActive', 
            'shortStartWrActive',
            'shortStartWinsCountActive',
            'shortStartLostCountActive', 
            'shortStartCountActive', 

            'longEndPnlActive',
            'longEndWrActive', 
            'longEndWinsActive', 
            'longEndLostActive', 
            'longEndCountActive', 

            'shortEndPnlActive',
            'shortEndWrActive', 
            'shortEndWinsCountActive', 
            'shortEndLostCountActive',
            'shortEndCountActive', 

            'longToShortPnlActive', 
            'longToShortWrActive', 
            'longToShortWinCountActive', 
            'longToShortLostCountActive',
            'longToShortCountActive',

            'longToLongPnlActive',
            'longToLongWrActive',
            'longToLongWinCountActive', 
            'longToLongLostCountActive',
            'longToLongCountActive', 

            'shortToLongPnlActive',
            'shortToLongWrActive',
            'shortToLongWinCountActive', 
            'shortToLongLostCountActive', 
            'shortToLongCountActive', 

            'shortToShortPnlActive', 
            'shortToShortWrActive',
            'shortToShortWinCountActive', 
            'shortToShortLostCountActive', 
            'shortToShortCountActive', 



            # Invesment
            'roiPctTotal',
            'roiPctHighTotal',
            'roiPctLowTotal',
            
            'largestWin',
            'largestLost',

            'avgWin',
            'avgLost',

            'closedRoiPct',

            'winsTotalRoiPct',
            'winsHighestRoiPct',
            'winslowestRoiPct',

            'lossesTotalRoiPct',
            'lossesHighestRoiPct',
            'lossesLowestRoiPct',

            'largestInvestment',
            'smallestInvestment',
            'averageInvestment',

            'largestReturn',
            'smallestReturn',
            'averageReturn',

            'largestRisk',
            'smallestRisk',
            'averageRisk',

            'largestReward',
            'smallestReward',
            'averageReward',

            # Pivot
            'longestAtoB',
            'shortestAtoB',
            'avgAToB',

            'longestBtoC',
            'shortestBtoC', 
            'avgBtoC', 

            'longestCtoD', 
            'shortestCtoD',
            'avgCtoD',

            'longestAtoD', 
            'shortestAtoD',
            'avgAtoD',
        )
        model = statistics
