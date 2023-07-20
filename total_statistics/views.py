from rest_framework import generics
from .serializers import StatisticsSerializer
from .models import statistics
from trade.models import all_trades
from django.http import HttpResponse
from typing import Union

class Trades():
    def __init__(self):
        self.all_entries = all_trades.objects.all().values()  

    def getTotalTradesCount(self):
        return

    def getExchangesTotalCount(self) -> Union[str,str,str,str]:

        nasdaq: int = 0
        forex: int = 0
        crypto: int = 0
        options: int = 0
 
        # for each in self.all_entries:
        
        #     if each['exchange'] == 'Nasdaq':
        #         nasdaq += 1
        #     if each['exchange'] == 'Forex':
        #         forex += 1
        #     if each['exchange'] == 'Crypto':
        #         crypto += 1
        #     if each['exchange'] == 'Options':
        #         options += 1

        return nasdaq, forex, crypto, options
    
    def getExchangesClosedCount(self) -> Union[str,str,str,str]:

        nasdaq: int = 0
        forex: int = 0
        crypto: int = 0
        options: int = 0
 
        for each in self.all_entries:
            if each['tradeClosed'] == 'True':
                if each['exchange'] == 'Nasdaq':
                    nasdaq += 1
                if each['exchange'] == 'Forex':
                    forex += 1
                if each['exchange'] == 'Crypto':
                    crypto += 1
                if each['exchange'] == 'Options':
                    options += 1

        return nasdaq, forex, crypto, options

    def getExchangesActiveCount(self) -> Union[str,str,str,str]:

        nasdaq: int = 0
        forex: int = 0
        crypto: int = 0
        options: int = 0
 
        for each in self.all_entries:
            if each['tradeOpen'] == 'True':
                if each['exchange'] == 'Nasdaq':
                    nasdaq += 1
                if each['exchange'] == 'Forex':
                    forex += 1
                if each['exchange'] == 'Crypto':
                    crypto += 1
                if each['exchange'] == 'Options':
                    options += 1


        return nasdaq, forex, crypto, options
    
    def get_all_trades_count(self) -> Union[int, int]:

        open: int = 0     
        closed: int = 0     
        for each in self.all_entries:  

      

            if(each['tradeInfo']['tradeOpen'] == True):
                open += 1
            if(each['tradeInfo']['tradeClosed'] == True):
                closed += 1
        total = open + closed

        return total, open, closed
       
    def getStartAndEndTypeCount(self, type: str) -> Union[int, int]:

        long = 0
        short = 0
        for each in self.all_entries:
            if each['openingTradeType'] == 'Bull':
                long += 1
            if each['openingTradeType'] == 'Bear':
                short += 1
            
        return short, long

    def getCompleteTradeCount(self) -> Union[int, int, int, int]:

        shortToLong: int = 0
        longToShort: int = 0
        shortToShort: int = 0
        longToLong: int = 0

        
        for each in self.all_entries:
       
            if each['completeTradeType'] == 'Bull-Bear':
                longToShort += 1

            if each['completeTradeType'] == 'Bear-Bull':
                shortToLong += 1
            
            if each['completeTradeType'] == 'Bull-Bull':
                longToLong += 1
                
            if each['completeTradeType'] == 'Bear-Bear':
                shortToShort += 1

        return shortToLong, longToShort, shortToShort, longToLong

class Performance():
    def __init__(self):
        self.all_entries = trade.objects.all().values()  

    def get_closed_and_active_performance_details(self, type: str) -> Union[float, float, int, int]:

        winning: int = 0
        losing: int = 0
        count: int = 0
        pnl: int = 0    
        winPct: int = 0   

        for each in self.all_entries:       

            if(each['tradeInfo'][type] == True):
                count += 1

                if(float(each['pnl']['pnl']) < (0)):
                    losing +=1
      
                if(float(each['pnl']['pnl']) > (0)):
                    winning += 1
                
                pnl += float(each['pnl']['pnl'])

        if (count > 0):
            winPct = (winning / count)  * 100

        return round(pnl,2), round(winPct,2), winning, losing
    
    def get_long_and_short_total_performance_details(self, type: str, market: str) -> Union[float, float, int, int, int]:

        count: int = 0
        wins: int = 0
        lost: int = 0
        pnl: int = 0

        for each in self.all_entries:
            if each[type] == market:

                count += 1

                if each['tradeResult'] == 'Win':
                    wins += 1

                if each['tradeResult'] == 'Loss':
                    lost += 1

                pnl += float(each['pnl'])

        winPct = (wins / len(self.all_entries)) * 100

    
        
        return round(pnl,2), round(winPct,2), wins, lost, count

    def get_long_and_short_closed_performance_details(self, type: str, market: str) -> Union[float, float, int, int, int]:

            count: int = 0
            wins: int = 0
            lost: int = 0
            pnl: int = 0

            for each in self.all_entries:
                if each['tradeClosed'] == 'True':
                    
                    if each[type] == market:
                        

                        count += 1
                        

                        if each['tradeResult'] == 'Win':
                            wins += 1

                        if each['tradeResult'] == 'Loss':
                            lost += 1

                        pnl += float(each['pnl'])

            winPct = (wins / len(self.all_entries)) * 100
                
            return round(pnl,2), round(winPct,2), wins, lost, count

    def get_long_and_short_active_performance_details(self, type: str, market: str) -> Union[float, float, int, int, int]:

            count: int = 0
            wins: int = 0
            lost: int = 0
            pnl: int = 0

            for each in self.all_entries:
                if each['tradeOpen'] == 'True':
                    if each[type] == market:

                        count += 1

                        if each['tradeResult'] == 'Win':
                            wins += 1

                        if each['tradeResult'] == 'Loss':
                            lost += 1

                        pnl += float(each['pnl'])

            winPct = (wins / len(self.all_entries)) * 100
                
            return round(pnl,2), round(winPct,2), wins, lost, count

class Investments():

    def __init__(self) -> None:
        self.all_entries = trade.objects.all().values()

    def get_closed_roi_average(self) -> float:

        returns = []
        for each in (self.all_entries):
            if(each['tradeClosed'] == 'True'):
                returns.append(float(each['returnPercentage']))
        
        avg = sum(returns) / len(returns)
     
        return '%.2f'%avg
    
    def get_wins_losses_roi_details(self, type) -> Union[float, float, float]:

        returns = []
        for each in (self.all_entries):
            if each['tradeResult'] == type:
                returns.append(float(each['returnPercentage']))
        
        if len(returns) > 0:
            avg = sum(returns) / len(returns) 
            high = max(returns)
            low = min(returns)
        else:
            avg = 0
            high = 0
            low = 0
   
  
        return '%.2f'%avg, '%.2f'%high, '%.2f'%low
    
        
    def get_roi_pct_total(self) -> Union[float, float, float]:

        returns = []
        for each in (self.all_entries):
            returns.append(float(each['returnPercentage']))
        
        if len(returns) > 0:
            avg = sum(returns) / len(returns) 
            high = max(returns)
            low = min(returns)
        else:
            avg = 0
            high = 0
            low = 0
   
  
        return '%.2f'%avg, '%.2f'%high, '%.2f'%low

    def get_largest_win_and_lost(self) -> Union[float, float]:

        largestWin = 0
        largestLost = 0

        for each in self.all_entries:
            if(float(each['pnl']['pnl']) > float(largestWin)):
                largestWin = each['pnl']['pnl']
            
            if(float(each['pnl']['pnl']) < float(largestLost)):
                largestLost = each['pnl']['pnl']

        return round(float(largestWin),2), round(float(largestLost),2)

    def get_average_win_and_lost(self) -> float:

        wins = []
        lost = []

        for each in self.all_entries:
            if each['tradeInfo']['tradeResult'] == 'Win':
                wins.append(float(each['pnl']['pnl']))

            if each['tradeInfo']['tradeResult'] == 'Loss':
                lost.append(float(each['pnl']['pnl']))

        avgWin = 0
        if len(wins) > 0:
            avgWin = sum(wins) / len(wins)
                     
        avgLost = 0
        if len(lost) > 0:
            avgLost = sum(lost) / len(lost)

        return round(avgWin,2), round(avgLost,2)

    def get_amount_invested_details(self) -> Union[int, int, float]:

        prices = []
        avg = 0
        largest = 0
        smallest = 0

        
        for each in self.all_entries:
            
            if each['tradeClosed'] == 'True':

             
                prices.append(float(each['priceOfC']))

        if len(prices) > 0:
            avg = round(sum(prices) / len(prices),2)
            largest = max(prices)
            smallest = min(prices)


        return largest, smallest, avg

    def get_amount_returned_details(self) -> Union[int, int, float]:

        prices = []
        avg = 0
        largest = 0
        smallest = 0

        for each in self.all_entries:
            if each['tradeClosed'] == 'True':
                prices.append(float(each['pnl']))

        if len(prices) > 0:
            avg = round(sum(prices) / len(prices),2)
            largest = max(prices)
            smallest = min(prices)

        return largest, smallest, avg

    def get_amount_risked_details(self) -> Union[int, int, float]:

        prices = []

        for each in self.all_entries:
            if each['tradeClosed'] == 'True':
            
                prices.append(float(each['risk']))

        avg = sum(prices) / len(prices)
        largest = max(prices)
        smallest = min(prices)
        
        return largest, smallest, round(avg,2)
     
    def get_amount_reward_details(self) -> Union[int, int, float]:

        prices = []

        for each in self.all_entries:
            prices.append(float(each['reward']))

        avg = sum(prices) / len(prices)
        largest = max(prices)
        smallest = min(prices)
        
        return largest, smallest, round(avg,2)

class Pivots():
    def __init__(self) -> None:
        self.all_entries = trade.objects.all().values()  

    def get_all_durations(self, ele) -> Union[float, float, float]:
    
        longest: int = 0
        shortest: int = 10000
        all = []
 
        for each in self.all_entries:

            if (abs(int(each[ele])) > longest):
                longest = abs(int(each[ele]))

            if (abs(int(each[ele])) < shortest):
                shortest = abs(int(each[ele]))

            all.append(abs(int(each[ele])))
        avg = sum(all) / len(all)

        return round(longest,2), round(shortest,2), round(avg,2)

def createStatistics(request):

    statistics.objects.all().delete()


    trades = Trades()

    # nasdaqTotalCount, forexTotalCount, cryptoTotalCount, optionsTotalCount = trades.getExchangesTotalCount()
    # nasdaqClosedCount, forexClosedCount, cryptoClosedCount, optionsClosedCount = trades.getExchangesClosedCount()
    # nasdaqActiveCount, forexActiveCount, cryptoActiveCount, optionsActiveCount = trades.getExchangesActiveCount()
    totalTradesCount, activeTradesCount, closedTradesCount = trades.get_all_trades_count()
    
    if(totalTradesCount > 0):
        performance = Performance()
        activePnl, activeWr, activeWinningCount, activeLosingCount = performance.get_closed_and_active_performance_details('tradeOpen')
        closedPnl, closedWr, closedWinCount, closedLostCount = performance.get_closed_and_active_performance_details('tradeClosed')
        totalPnl = "%.2f"%(activePnl + closedPnl)
        totalAvgReturn = "%.2f"%(float(totalPnl) / totalTradesCount)
        totalWr = "%.0f"%(((activeWinningCount + closedWinCount) / totalTradesCount) * 100)
        totalWinCount = (activeWinningCount + closedWinCount)
        totalLostCount = (activeLosingCount + closedLostCount)
        
        # shortToLongPnlTotal, shortToLongWrTotal, shortToLongWinCountTotal, shortToLongLostCountTotal, shortToLongCountTotal = performance.get_long_and_short_total_performance_details('completeTradeType','Bear-Bull')
        # shortToShortPnlTotal, shortToShortWrTotal, shortToShortWinCountTotal, shortToShortLostCountTotal, shortToShortCountTotal = performance.get_long_and_short_total_performance_details('completeTradeType','Bear-Bear')
        # longToShortPnlTotal, longToShortWrTotal, longToShortWinCountTotal, longToShortLostCountTotal, longToShortCountTotal = performance.get_long_and_short_total_performance_details('completeTradeType','Bull-Bear')
        # longToLongPnlTotal, longToLongWrTotal, longToLongWinCountTotal, longToLongLostCountTotal, longToLongCountTotal = performance.get_long_and_short_total_performance_details('completeTradeType','Bull-Bull')
        # longStartPnlTotal, longStartWrTotal, longStartWinsCountTotal, longStartLostCountTotal, longStartCountTotal = performance.get_long_and_short_total_performance_details('openingTradeType', 'Bull')
        # shortStartPnlTotal, shortStartWrTotal, shortStartWinsCountTotal, shortStartLostCountTotal, shortStartCountTotal = performance.get_long_and_short_total_performance_details('openingTradeType', 'Bear')
        # longEndPnlTotal, longEndWrTotal, longEndWinsTotal, longEndLostTotal, longEndCountTotal = performance.get_long_and_short_total_performance_details('closingTradeType', 'Bull')
        # shortEndPnlTotal, shortEndWrTotal, shortEndWinsCountTotal, shortEndLostCountTotal, shortEndCountTotal = performance.get_long_and_short_total_performance_details('closingTradeType', 'Bear')
        
        # longStartPnlClosed, longStartWrClosed, longStartWinsCountClosed, longStartLostCountClosed, longStartCountClosed = performance.get_long_and_short_closed_performance_details('openingTradeType', 'Bull')
        # shortStartPnlClosed, shortStartWrClosed, shortStartWinsCountClosed, shortStartLostCountClosed, shortStartCountClosed = performance.get_long_and_short_closed_performance_details('openingTradeType', 'Bear')
        # longEndPnlClosed, longEndWrClosed, longEndWinsClosed, longEndLostClosed, longEndCountClosed = performance.get_long_and_short_closed_performance_details('closingTradeType', 'Bull')
        # shortEndPnlClosed, shortEndWrClosed, shortEndWinsCountClosed, shortEndLostCountClosed, shortEndCountClosed = performance.get_long_and_short_closed_performance_details('closingTradeType', 'Bear')
        # longToShortPnlClosed, longToShortWrClosed, longToShortWinCountClosed, longToShortLostCountClosed, longToShortCountClosed = performance.get_long_and_short_closed_performance_details('completeTradeType','Bull-Bear')
        # longToLongPnlClosed, longToLongWrClosed, longToLongWinCountClosed, longToLongLostCountClosed, longToLongCountClosed = performance.get_long_and_short_closed_performance_details('completeTradeType','Bull-Bull')
        # shortToLongPnlClosed, shortToLongWrClosed, shortToLongWinCountClosed, shortToLongLostCountClosed, shortToLongCountClosed = performance.get_long_and_short_closed_performance_details('completeTradeType','Bear-Bull')
        # shortToShortPnlClosed, shortToShortWrClosed, shortToShortWinCountClosed, shortToShortLostCountClosed, shortToShortCountClosed = performance.get_long_and_short_closed_performance_details('completeTradeType','Bear-Bear')

        # longStartPnlActive, longStartWrActive, longStartWinsCountActive, longStartLostCountActive, longStartCountActive = performance.get_long_and_short_active_performance_details('openingTradeType', 'Bull')
        # shortStartPnlActive, shortStartWrActive, shortStartWinsCountActive, shortStartLostCountActive, shortStartCountActive = performance.get_long_and_short_active_performance_details('openingTradeType', 'Bear')
        # longEndPnlActive, longEndWrActive, longEndWinsActive, longEndLostActive, longEndCountActive = performance.get_long_and_short_active_performance_details('closingTradeType', 'Bull')
        # shortEndPnlActive, shortEndWrActive, shortEndWinsCountActive, shortEndLostCountActive, shortEndCountActive = performance.get_long_and_short_active_performance_details('closingTradeType', 'Bear')
        # longToShortPnlActive, longToShortWrActive, longToShortWinCountActive, longToShortLostCountActive, longToShortCountActive = performance.get_long_and_short_active_performance_details('completeTradeType','Bull-Bear')
        # longToLongPnlActive, longToLongWrActive, longToLongWinCountActive, longToLongLostCountActive, longToLongCountActive = performance.get_long_and_short_active_performance_details('completeTradeType','Bull-Bull')
        # shortToLongPnlActive, shortToLongWrActive, shortToLongWinCountActive, shortToLongLostCountActive, shortToLongCountActive = performance.get_long_and_short_active_performance_details('completeTradeType','Bear-Bull')
        # shortToShortPnlActive, shortToShortWrActive, shortToShortWinCountActive, shortToShortLostCountActive, shortToShortCountActive = performance.get_long_and_short_active_performance_details('completeTradeType','Bear-Bear')
        
        
        # investment = Investments()
    
        # largestWin, largestLost = investment.get_largest_win_and_lost()    
        # avgWin, avgLost = investment.get_average_win_and_lost()
        # roiPctTotal, roiPctHighTotal, roiPctLowTotal = investment.get_roi_pct_total()
        # closedRoiPct = investment.get_closed_roi_average()
        # winsTotalRoiPct, winsHighestRoiPct, winslowestRoiPct, = investment.get_wins_losses_roi_details('Win')
        # lossesTotalRoiPct, lossesHighestRoiPct, lossesLowestRoiPct, = investment.get_wins_losses_roi_details('Loss')
        # largestInvestment, smallestInvestment, averageInvestment = investment.get_amount_invested_details()
        # largestReturn, smallestReturn, averageReturn = investment.get_amount_returned_details()
        # largestRisk, smallestRisk, averageRisk = investment.get_amount_risked_details()
        # largestReward, smallestReward, averageReward = investment.get_amount_reward_details()
    
        # pivots = Pivots()
        # longestAtoB, shortestAtoB, avgAToB = pivots.get_all_durations('length_AtoB')
        # longestBtoC, shortestBtoC, avgBtoC = pivots.get_all_durations('length_BtoC')
        # longestCtoD, shortestCtoD, avgCtoD = pivots.get_all_durations('length_CtoD')
        # longestAtoD, shortestAtoD, avgAtoD = pivots.get_all_durations('length_AtoD')

        statistics.objects.get_or_create(
            
            # # Trades
            # nasdaqTotalCount = nasdaqTotalCount, 
            # forexTotalCount = forexTotalCount,
            # cryptoTotalCount = cryptoTotalCount,
            # optionsTotalCount = optionsTotalCount,

            # nasdaqClosedCount = nasdaqClosedCount, 
            # forexClosedCount = forexClosedCount,
            # cryptoClosedCount = cryptoClosedCount,
            # optionsClosedCount = optionsClosedCount,

            # nasdaqActiveCount = nasdaqActiveCount, 
            # forexActiveCount = forexActiveCount,
            # cryptoActiveCount = cryptoActiveCount,
            # optionsActiveCount = optionsActiveCount,

            # totalTradesCount = totalTradesCount,
            # activeTradesCount = activeTradesCount,
            # closedTradesCount = closedTradesCount,

            # # Peformance
            # activePnl = activePnl,
            # activeWr = activeWr,
            # activeWinningCount = activeWinningCount,
            # activeLosingCount = activeLosingCount,

            # closedPnl = closedPnl,
            # closedWr = closedWr,
            # closedWinCount = closedWinCount,
            # closedLostCount = closedLostCount,

            totalPnl = totalPnl,
            totalWr = totalWr,
            totalWinCount = totalWinCount,
            totalLostCount = totalLostCount,
            totalAvgReturn = totalAvgReturn,

            # longStartPnlTotal = longStartPnlTotal,
            # longStartWrTotal = longStartWrTotal,
            # longStartWinsCountTotal = longStartWinsCountTotal,
            # longStartLostCountTotal = longStartLostCountTotal,
            # longStartCountTotal = longStartCountTotal,

            # shortStartPnlTotal = shortStartPnlTotal,
            # shortStartWrTotal = shortStartWrTotal,
            # shortStartWinsCountTotal = shortStartWinsCountTotal,
            # shortStartLostCountTotal  = shortStartLostCountTotal, 
            # shortStartCountTotal = shortStartCountTotal,

            # longEndPnlTotal = longEndPnlTotal,
            # longEndWrTotal = longEndWrTotal,
            # longEndWinsTotal = longEndWinsTotal,
            # longEndLostTotal = longEndLostTotal,
            # longEndCountTotal = longEndCountTotal,

            # shortEndPnlTotal = shortEndPnlTotal,
            # shortEndWrTotal = shortEndWrTotal,
            # shortEndWinsCountTotal = shortEndWinsCountTotal,
            # shortEndLostCountTotal = shortEndLostCountTotal,
            # shortEndCountTotal = shortEndCountTotal,

            # longToShortPnlTotal = longToShortPnlTotal,
            # longToShortWrTotal = longToShortWrTotal,
            # longToShortWinCountTotal = longToShortWinCountTotal,
            # longToShortLostCountTotal = longToShortLostCountTotal,
            # longToShortCountTotal = longToShortCountTotal,

            # longToLongPnlTotal = longToLongPnlTotal,
            # longToLongWrTotal = longToLongWrTotal,
            # longToLongWinCountTotal = longToLongWinCountTotal,
            # longToLongLostCountTotal = longToLongLostCountTotal,
            # longToLongCountTotal = longToLongCountTotal,

            # shortToLongPnlTotal = shortToLongPnlTotal,
            # shortToLongWrTotal = shortToLongWrTotal,
            # shortToLongWinCountTotal = shortToLongWinCountTotal,
            # shortToLongLostCountTotal = shortToLongLostCountTotal,
            # shortToLongCountTotal = shortToLongCountTotal,

            # shortToShortPnlTotal = shortToShortPnlTotal,
            # shortToShortWrTotal = shortToShortWrTotal,
            # shortToShortWinCountTotal = shortToShortWinCountTotal,
            # shortToShortLostCountTotal = shortToShortLostCountTotal,
            # shortToShortCountTotal = shortToShortCountTotal,
            
            # longStartPnlClosed = longStartPnlClosed,
            # longStartWrClosed  = longStartWrClosed,
            # longStartWinsCountClosed  = longStartWinsCountClosed,
            # longStartLostCountClosed  = longStartLostCountClosed,
            # longStartCountClosed  = longStartCountClosed,

            # shortStartPnlClosed = shortStartPnlClosed ,
            # shortStartWrClosed = shortStartWrClosed ,
            # shortStartWinsCountClosed = shortStartWinsCountClosed ,
            # shortStartLostCountClosed  = shortStartLostCountClosed , 
            # shortStartCountClosed = shortStartCountClosed ,

            # longEndPnlClosed = longEndPnlClosed ,
            # longEndWrClosed = longEndWrClosed ,
            # longEndWinsClosed = longEndWinsClosed ,
            # longEndLostClosed = longEndLostClosed ,
            # longEndCountClosed = longEndCountClosed ,

            # shortEndPnlClosed = shortEndPnlClosed ,
            # shortEndWrClosed = shortEndWrClosed ,
            # shortEndWinsCountClosed = shortEndWinsCountClosed ,
            # shortEndLostCountClosed = shortEndLostCountClosed ,
            # shortEndCountClosed = shortEndCountClosed ,

            # longToShortPnlClosed = longToShortPnlClosed ,
            # longToShortWrClosed = longToShortWrClosed ,
            # longToShortWinCountClosed = longToShortWinCountClosed ,
            # longToShortLostCountClosed = longToShortLostCountClosed ,
            # longToShortCountClosed = longToShortCountClosed ,

            # longToLongPnlClosed = longToLongPnlClosed ,
            # longToLongWrClosed = longToLongWrClosed ,
            # longToLongWinCountClosed = longToLongWinCountClosed ,
            # longToLongLostCountClosed = longToLongLostCountClosed ,
            # longToLongCountClosed = longToLongCountClosed ,

            # shortToLongPnlClosed = shortToLongPnlClosed ,
            # shortToLongWrClosed = shortToLongWrClosed ,
            # shortToLongWinCountClosed = shortToLongWinCountClosed ,
            # shortToLongLostCountClosed = shortToLongLostCountClosed ,
            # shortToLongCountClosed = shortToLongCountClosed ,

            # shortToShortPnlClosed = shortToShortPnlClosed ,
            # shortToShortWrClosed = shortToShortWrClosed ,
            # shortToShortWinCountClosed = shortToShortWinCountClosed ,
            # shortToShortLostCountClosed = shortToShortLostCountClosed ,
            # shortToShortCountClosed = shortToShortCountClosed ,

            # longStartPnlActive = longStartPnlActive,
            # longStartWrActive  = longStartWrActive,
            # longStartWinsCountActive  = longStartWinsCountActive,
            # longStartLostCountActive  = longStartLostCountActive,
            # longStartCountActive  = longStartCountActive,

            # shortStartPnlActive = shortStartPnlActive ,
            # shortStartWrActive = shortStartWrActive ,
            # shortStartWinsCountActive = shortStartWinsCountActive ,
            # shortStartLostCountActive  = shortStartLostCountActive , 
            # shortStartCountActive = shortStartCountActive ,

            # longEndPnlActive = longEndPnlActive ,
            # longEndWrActive = longEndWrActive ,
            # longEndWinsActive = longEndWinsActive ,
            # longEndLostActive = longEndLostActive ,
            # longEndCountActive = longEndCountActive ,

            # shortEndPnlActive = shortEndPnlActive ,
            # shortEndWrActive = shortEndWrActive ,
            # shortEndWinsCountActive = shortEndWinsCountActive ,
            # shortEndLostCountActive = shortEndLostCountActive ,
            # shortEndCountActive = shortEndCountActive ,

            # longToShortPnlActive = longToShortPnlActive ,
            # longToShortWrActive = longToShortWrActive ,
            # longToShortWinCountActive = longToShortWinCountActive ,
            # longToShortLostCountActive = longToShortLostCountActive ,
            # longToShortCountActive = longToShortCountActive ,

            # longToLongPnlActive = longToLongPnlActive ,
            # longToLongWrActive = longToLongWrActive ,
            # longToLongWinCountActive = longToLongWinCountActive ,
            # longToLongLostCountActive = longToLongLostCountActive ,
            # longToLongCountActive = longToLongCountActive ,

            # shortToLongPnlActive = shortToLongPnlActive ,
            # shortToLongWrActive = shortToLongWrActive ,
            # shortToLongWinCountActive = shortToLongWinCountActive ,
            # shortToLongLostCountActive = shortToLongLostCountActive ,
            # shortToLongCountActive = shortToLongCountActive ,

            # shortToShortPnlActive = shortToShortPnlActive ,
            # shortToShortWrActive = shortToShortWrActive ,
            # shortToShortWinCountActive = shortToShortWinCountActive ,
            # shortToShortLostCountActive = shortToShortLostCountActive ,
            # shortToShortCountActive = shortToShortCountActive ,

            # Investment

            # roiPctTotal = roiPctTotal,
            # roiPctHighTotal = roiPctHighTotal,
            # roiPctLowTotal = roiPctLowTotal,

            # largestWin = largestWin,
            # largestLost = largestLost,

            # avgWin = avgWin,
            # avgLost = avgLost,

            # closedRoiPct = closedRoiPct,

            # winsTotalRoiPct = winsTotalRoiPct,
            # winsHighestRoiPct = winsHighestRoiPct,
            # winslowestRoiPct = winslowestRoiPct,

            # lossesTotalRoiPct = lossesTotalRoiPct,
            # lossesHighestRoiPct = lossesHighestRoiPct,
            # lossesLowestRoiPct = lossesLowestRoiPct,

            # largestInvestment = largestInvestment,
            # smallestInvestment = smallestInvestment,
            # averageInvestment = averageInvestment,

            # largestReturn = largestReturn,
            # smallestReturn = smallestReturn,
            # averageReturn = averageReturn,

            # largestRisk = largestRisk,
            # smallestRisk = smallestRisk,
            # averageRisk = averageRisk,

            # largestReward = largestReward,
            # smallestReward = smallestReward,
            # averageReward = averageReward,

            # Pivot
            
            # longestAtoB = longestAtoB,
            # shortestAtoB = shortestAtoB,
            # avgAToB = avgAToB,

            # longestBtoC = longestBtoC,
            # shortestBtoC = shortestBtoC,
            # avgBtoC = avgBtoC,

            # longestCtoD = longestCtoD,
            # shortestCtoD = shortestCtoD,
            # avgCtoD = avgCtoD,

            # longestAtoD = longestAtoD,
            # shortestAtoD = shortestAtoD,
            # avgAtoD = avgAtoD
        )
        
    elif(totalTradesCount == 0):
        print('createStatistics: NO TRADES.')

        
    
    return HttpResponse('saveStrategySettings')

class statisticsModels(generics.ListCreateAPIView):
    queryset            = statistics.objects.all()
    serializer_class    = StatisticsSerializer