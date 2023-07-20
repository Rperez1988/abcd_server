from unittest.util import _MAX_LENGTH
from django.db import models

class statistics(models.Model):

    # Trades
    nasdaqTotalCount = models.CharField(('nasdaqTotalCount'), max_length=255)
    forexTotalCount = models.CharField(('forexTotalCount'), max_length=255)
    cryptoTotalCount = models.CharField(('cryptoTotalCount'), max_length=255)
    optionsTotalCount = models.CharField(('optionsTotalCount'), max_length=255)

    nasdaqClosedCount = models.CharField(('nasdaqClosedCount'), max_length=255)
    forexClosedCount = models.CharField(('forexClosedCount'), max_length=255)
    cryptoClosedCount = models.CharField(('cryptoClosedCount'), max_length=255)
    optionsClosedCount = models.CharField(('optionsClosedCount'), max_length=255)

    nasdaqActiveCount = models.CharField(('nasdaqActiveCount'), max_length=255)
    forexActiveCount = models.CharField(('forexActiveCount'), max_length=255)
    cryptoActiveCount = models.CharField(('cryptoActiveCount'), max_length=255)
    optionsActiveCount = models.CharField(('optionsActiveCount'), max_length=255)

    totalTradesCount = models.CharField(('totalTradesCount'), max_length=255)
    activeTradesCount = models.CharField(('activeTradesCount'), max_length=255)
    closedTradesCount = models.CharField(('closedTradesCount'), max_length=255)

    # Peformance  
    activePnl = models.CharField(('activePnl'), max_length=255)
    activeWr = models.CharField(('activeWr'), max_length=255)
    activeWinningCount = models.CharField(('activeWinningCount'),max_length=255)
    activeLosingCount = models.CharField(('activeLosingCount'), max_length=255)

    closedPnl = models.CharField(('closedPnl'), max_length=255)
    closedWr = models.CharField(('closedWr'), max_length=255)
    closedWinCount = models.CharField(('closedWinCount'), max_length=255)
    closedLostCount = models.CharField(('closedLostCount'), max_length=255)

    totalPnl = models.CharField(('totalPnl'), max_length=255)
    totalWr = models.CharField(('totalWr'), max_length=255)
    totalWinCount = models.CharField(('totalWinCount'), max_length=255)
    totalLostCount = models.CharField(('totalLostCount'), max_length=255)
    totalAvgReturn = models.CharField(('totalAvgReturn'), max_length=255)

    longStartPnlTotal = models.CharField(('longStartPnlTotal'), max_length=255)
    longStartWrTotal = models.CharField(('longStartWrTotal'), max_length=255)
    longStartWinsCountTotal = models.CharField(('longStartWinsCountTotal'),max_length=255)
    longStartLostCountTotal = models.CharField(('longStartLostCountTotal'), max_length=255)
    longStartCountTotal = models.CharField(('longStartCountTotal'), max_length=255)

    shortStartPnlTotal = models.CharField(('shortStartPnlTotal'), max_length=255)
    shortStartWrTotal = models.CharField(('shortStartWrTotal'), max_length=255)
    shortStartWinsCountTotal = models.CharField(('shortStartWinsCountTotal'), max_length=255)
    shortStartLostCountTotal = models.CharField(('shortStartLostCountTotal'), max_length=255)
    shortStartCountTotal = models.CharField(('shortStartCountTotal'), max_length=255)

    longEndPnlTotal = models.CharField(('longEndPnlTotal'),max_length=255)
    longEndWrTotal = models.CharField(('longEndWrTotal'), max_length=255)
    longEndWinsTotal = models.CharField(('longEndWinsTotal'), max_length=255)
    longEndLostTotal = models.CharField(('longEndLostTotal'), max_length=255)
    longEndCountTotal = models.CharField(('longEndCountTotal'), max_length=255)

    shortEndPnlTotal = models.CharField(('shortEndPnlTotal'), max_length=255)
    shortEndWrTotal = models.CharField(('shortEndWrTotal'), max_length=255)
    shortEndWinsCountTotal= models.CharField(('shortEndWinsCountTotal'), max_length=255)
    shortEndLostCountTotal = models.CharField(('shortEndLostCountTotal'), max_length=255)
    shortEndCountTotal = models.CharField(('shortEndCountTotal'), max_length=255)

    longToShortPnlTotal = models.CharField(('longToShortPnlTotal'), max_length=255)
    longToShortWrTotal = models.CharField(('longToShortWrTotal'), max_length=255)
    longToShortWinCountTotal= models.CharField(('longToShortWinCountTotal'), max_length=255)
    longToShortLostCountTotal = models.CharField(('longToShortLostCountTotal'), max_length=255)
    longToShortCountTotal = models.CharField(('longToShortCountTotal'), max_length=255)

    longToLongPnlTotal = models.CharField(('longToLongPnlTotal'), max_length=255)
    longToLongWrTotal = models.CharField(('longToLongWrTotal'), max_length=255)
    longToLongWinCountTotal = models.CharField(('longToLongWinCountTotal'), max_length=255)
    longToLongLostCountTotal = models.CharField(('longToLongLostCountTotal'), max_length=255)
    longToLongCountTotal = models.CharField(('longToLongCountTotal'), max_length=255)

    shortToLongPnlTotal = models.CharField(('shortToLongPnlTotal'), max_length=255)
    shortToLongWrTotal = models.CharField(('shortToLongWrTotal'), max_length=255)
    shortToLongWinCountTotal = models.CharField(('shortToLongWinCountTotal'), max_length=255)
    shortToLongLostCountTotal = models.CharField(('shortToLongLostCountTotal'), max_length=255)
    shortToLongCountTotal = models.CharField(('shortToLongCountTotal'), max_length=255)

    shortToShortPnlTotal = models.CharField(('shortToShortPnlTotal'), max_length=255)
    shortToShortWrTotal = models.CharField(('shortToShortWrTotal'), max_length=255)
    shortToShortWinCountTotal = models.CharField(('shortToShortWinCountTotal'), max_length=255)
    shortToShortLostCountTotal = models.CharField(('shortToShortLostCountTotal'), max_length=255)
    shortToShortCountTotal = models.CharField(('shortToShortCountTotal'), max_length=255)

    longStartPnlClosed = models.CharField(('longStartPnlClosed'), max_length=255)
    longStartWrClosed = models.CharField(('longStartWrClosed'), max_length=255)
    longStartWinsCountClosed = models.CharField(('longStartWinsCountClosed'),max_length=255)
    longStartLostCountClosed = models.CharField(('longStartLostCountClosed'), max_length=255)
    longStartCountClosed = models.CharField(('longStartCountClosed'), max_length=255)

    shortStartPnlClosed = models.CharField(('shortStartPnlClosed'), max_length=255)
    shortStartWrClosed = models.CharField(('shortStartWrClosed'), max_length=255)
    shortStartWinsCountClosed = models.CharField(('shortStartWinsCountClosed'), max_length=255)
    shortStartLostCountClosed = models.CharField(('shortStartLostCountClosed'), max_length=255)
    shortStartCountClosed = models.CharField(('shortStartCountClosed'), max_length=255)

    longEndPnlClosed = models.CharField(('longEndPnlClosed'),max_length=255)
    longEndWrClosed = models.CharField(('longEndWrClosed'), max_length=255)
    longEndWinsClosed = models.CharField(('longEndWinsClosed'), max_length=255)
    longEndLostClosed = models.CharField(('longEndLostClosed'), max_length=255)
    longEndCountClosed = models.CharField(('longEndCountClosed'), max_length=255)

    shortEndPnlClosed = models.CharField(('shortEndPnlClosed'), max_length=255)
    shortEndWrClosed = models.CharField(('shortEndWrClosed'), max_length=255)
    shortEndWinsCountClosed= models.CharField(('shortEndWinsCountClosed'), max_length=255)
    shortEndLostCountClosed = models.CharField(('shortEndLostCountClosed'), max_length=255)
    shortEndCountClosed = models.CharField(('shortEndCountClosed'), max_length=255)

    longToShortPnlClosed = models.CharField(('longToShortPnlClosed'), max_length=255)
    longToShortWrClosed = models.CharField(('longToShortWrClosed'), max_length=255)
    longToShortWinCountClosed= models.CharField(('longToShortWinCountClosed'), max_length=255)
    longToShortLostCountClosed = models.CharField(('longToShortLostCountClosed'), max_length=255)
    longToShortCountClosed = models.CharField(('longToShortCountClosed'), max_length=255)

    longToLongPnlClosed = models.CharField(('longToLongPnlClosed'), max_length=255)
    longToLongWrClosed = models.CharField(('longToLongWrClosed'), max_length=255)
    longToLongWinCountClosed = models.CharField(('longToLongWinCountClosed'), max_length=255)
    longToLongLostCountClosed = models.CharField(('longToLongLostCountClosed'), max_length=255)
    longToLongCountClosed = models.CharField(('longToLongCountClosed'), max_length=255)

    shortToLongPnlClosed = models.CharField(('shortToLongPnlClosed'), max_length=255)
    shortToLongWrClosed = models.CharField(('shortToLongWrClosed'), max_length=255)
    shortToLongWinCountClosed = models.CharField(('shortToLongWinCountClosed'), max_length=255)
    shortToLongLostCountClosed = models.CharField(('shortToLongLostCountClosed'), max_length=255)
    shortToLongCountClosed = models.CharField(('shortToLongCountClosed'), max_length=255)

    shortToShortPnlClosed = models.CharField(('shortToShortPnlClosed'), max_length=255)
    shortToShortWrClosed = models.CharField(('shortToShortWrClosed'), max_length=255)
    shortToShortWinCountClosed = models.CharField(('shortToShortWinCountClosed'), max_length=255)
    shortToShortLostCountClosed = models.CharField(('shortToShortLostCountClosed'), max_length=255)
    shortToShortCountClosed = models.CharField(('shortToShortCountClosed'), max_length=255)

    longStartPnlActive = models.CharField(('longStartPnlActive'), max_length=255)
    longStartWrActive = models.CharField(('longStartWrActive'), max_length=255)
    longStartWinsCountActive = models.CharField(('longStartWinsCountActive'),max_length=255)
    longStartLostCountActive = models.CharField(('longStartLostCountActive'), max_length=255)
    longStartCountActive = models.CharField(('longStartCountActive'), max_length=255)

    shortStartPnlActive = models.CharField(('shortStartPnlActive'), max_length=255)
    shortStartWrActive = models.CharField(('shortStartWrActive'), max_length=255)
    shortStartWinsCountActive = models.CharField(('shortStartWinsCountActive'), max_length=255)
    shortStartLostCountActive = models.CharField(('shortStartLostCountActive'), max_length=255)
    shortStartCountActive = models.CharField(('shortStartCountActive'), max_length=255)

    longEndPnlActive = models.CharField(('longEndPnlActive'),max_length=255)
    longEndWrActive = models.CharField(('longEndWrActive'), max_length=255)
    longEndWinsActive = models.CharField(('longEndWinsActive'), max_length=255)
    longEndLostActive = models.CharField(('longEndLostActive'), max_length=255)
    longEndCountActive = models.CharField(('longEndCountActive'), max_length=255)

    shortEndPnlActive = models.CharField(('shortEndPnlActive'), max_length=255)
    shortEndWrActive = models.CharField(('shortEndWrActive'), max_length=255)
    shortEndWinsCountActive= models.CharField(('shortEndWinsCountActive'), max_length=255)
    shortEndLostCountActive = models.CharField(('shortEndLostCountActive'), max_length=255)
    shortEndCountActive = models.CharField(('shortEndCountActive'), max_length=255)

    longToShortPnlActive = models.CharField(('longToShortPnlActive'), max_length=255)
    longToShortWrActive = models.CharField(('longToShortWrActive'), max_length=255)
    longToShortWinCountActive= models.CharField(('longToShortWinCountActive'), max_length=255)
    longToShortLostCountActive = models.CharField(('longToShortLostCountActive'), max_length=255)
    longToShortCountActive = models.CharField(('longToShortCountActive'), max_length=255)

    longToLongPnlActive = models.CharField(('longToLongPnlActive'), max_length=255)
    longToLongWrActive = models.CharField(('longToLongWrActive'), max_length=255)
    longToLongWinCountActive = models.CharField(('longToLongWinCountActive'), max_length=255)
    longToLongLostCountActive = models.CharField(('longToLongLostCountActive'), max_length=255)
    longToLongCountActive = models.CharField(('longToLongCountActive'), max_length=255)

    shortToLongPnlActive = models.CharField(('shortToLongPnlActive'), max_length=255)
    shortToLongWrActive = models.CharField(('shortToLongWrActive'), max_length=255)
    shortToLongWinCountActive = models.CharField(('shortToLongWinCountActive'), max_length=255)
    shortToLongLostCountActive = models.CharField(('shortToLongLostCountActive'), max_length=255)
    shortToLongCountActive = models.CharField(('shortToLongCountActive'), max_length=255)

    shortToShortPnlActive = models.CharField(('shortToShortPnlActive'), max_length=255)
    shortToShortWrActive = models.CharField(('shortToShortWrActive'), max_length=255)
    shortToShortWinCountActive = models.CharField(('shortToShortWinCountActive'), max_length=255)
    shortToShortLostCountActive = models.CharField(('shortToShortLostCountActive'), max_length=255)
    shortToShortCountActive = models.CharField(('shortToShortCountActive'), max_length=255)





    # Investment
    roiPctTotal = models.CharField(('roiPctTotal'), max_length=255)
    roiPctHighTotal = models.CharField(('roiPctHighTotal'), max_length=255)
    roiPctLowTotal = models.CharField(('roiPctLowTotal'), max_length=255)

    largestWin = models.CharField(('largestWin'), max_length=255)
    largestLost = models.CharField(('largestLost'), max_length=255)

    avgWin = models.CharField(('avgWin'), max_length=255)
    avgLost = models.CharField(('avgLost'), max_length=255)
    
    closedRoiPct = models.CharField(('closedRoiPct'), max_length=255)

    winsTotalRoiPct = models.CharField(('winsTotalRoiPct'), max_length=255)
    winsHighestRoiPct = models.CharField(('winsHighestRoiPct'), max_length=255)
    winslowestRoiPct = models.CharField(('winslowestRoiPct'), max_length=255)

 
    lossesTotalRoiPct = models.CharField(('lossesTotalRoiPct'), max_length=255)
    lossesHighestRoiPct = models.CharField(('lossesHighestRoiPct'), max_length=255)
    lossesLowestRoiPct = models.CharField(('lossesLowestRoiPct'), max_length=255)

    largestInvestment = models.CharField(('largestInvestment'), max_length=255)
    smallestInvestment = models.CharField(('smallestInvestment'), max_length=255)
    averageInvestment = models.CharField(('averageInvestment'), max_length=255)

    largestReturn = models.CharField(('largestReturn'), max_length=255)
    smallestReturn = models.CharField(('smallestReturn'), max_length=255)
    averageReturn = models.CharField(('averageReturn'), max_length=255)

    largestRisk = models.CharField(('largestRisk'), max_length=255)
    smallestRisk = models.CharField(('smallestRisk'), max_length=255)
    averageRisk = models.CharField(('averageRisk'), max_length=255)

    largestReward = models.CharField(('largestReward'), max_length=255)
    smallestReward = models.CharField(('smallestReward'), max_length=255)
    averageReward = models.CharField(('averageReward'), max_length=255)

    # Pivot
    longestAtoB = models.CharField(('longestAtoB'), max_length=255)
    shortestAtoB = models.CharField(('shortestAtoB'), max_length=255)
    avgAToB = models.CharField(('avgAToB'), max_length=255)

    longestBtoC = models.CharField(('longestBtoC'), max_length=255)
    shortestBtoC = models.CharField(('shortestBtoC'), max_length=255)
    avgBtoC = models.CharField(('avgBtoC'), max_length=255)

    longestCtoD = models.CharField(('longestCtoD'), max_length=255)
    shortestCtoD = models.CharField(('shortestCtoD'), max_length=255)
    avgCtoD = models.CharField(('avgCtoD'), max_length=255)

    longestAtoD = models.CharField(('longestAtoD'), max_length=255)
    shortestAtoD = models.CharField(('shortestAtoD'), max_length=255)
    avgAtoD = models.CharField(('avgAtoD'), max_length=255)




