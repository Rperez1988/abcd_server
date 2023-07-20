from operator import rshift
import re
# import bot.Results
import csv
import pandas       as pd
from .models        import stock, strategyResults, tradeResults, chartImage, stocksTested, totalResults, stockStatistics
from django.http    import HttpResponse
from os.path import exists
import os
import config
from datetime import datetime
from statistics                     import mean
import sys
# sys.path.append('../..')
import sys
# Add the ptdraft folder path to the sys.path list
# sys.path.append('App/Strategies')

def stockNameIntoCSV(stock):
    # Convert into QuerySet

    df = pd.DataFrame.from_records(list(stock.values()))
    df.columns = ['id','Date','Open', 'High', 'Low', 'Close', 'adj Close','volume','symbol']


    # querySet = stock.values_list('id','date','open', 'close', 'high', 'low', 'adjClose','volume')


    #  Convert into Pandas DF
    # df = pd.DataFrame(querySet, columns=['id','Date','Open', 'High', 'Low', 'Close', 'adj Close','volume'])

    # Remove id column
    del df['id']

    # Convert to CSV
    csv = df.to_csv(index=False)


    # Convert Dates to string
    df["Date"] = pd.to_datetime(df["Date"], format='%Y-%m-%d')
    df['Date'].dt.strftime('%Y-%m-%d')


    # Create CSV file
    with open('first.csv', 'x') as f:
        f.write(csv)
    df = pd.read_csv('C:/Users/rpere/Desktop/abcd/abcd_local/abcd_server/backend/first.csv')
    df.to_csv('second.csv', index=False)

    return df

def getUserInput(request, each):



    length              = getBodyContext(request, 'length')
    ticker              = each
    # ticker              = getBodyContext(request, 'stock')
    plBelowPh           = getBodyContext(request, 'plBelowPh')
    PHtoPLLength        = getBodyContext(request, 'PHtoPLLength')
    pLtoShortLength     = getBodyContext(request, 'pLtoShortLength')
    marketType          = getBodyContext(request, 'marketType')
    strategy            = getBodyContext(request, 'selectedRunStrategy')




    if plBelowPh == 'false':
        plBelowPh = False
    elif plBelowPh == 'true':
        plBelowPh == True

    return length, ticker, plBelowPh, PHtoPLLength, pLtoShortLength, marketType, strategy

def runBot(length, df, ticker, plBelowPh, PHtoPLLength, pLtoShortLength, marketType, strategy):
    print('hello')

def createTempFile(df):

    """Create csv file"""
    with open('first.csv', 'x') as f:
        f.write(csv)

    """Convert againt to remove new lines"""
    df = pd.read_csv('C:/Users/rpere/Desktop/abcd/abcd_local/abcd_server/backend/first.csv')
    df.to_csv('second.csv', index=False)

    return df
    
def deleteTempfiles():
    import os
    from os.path import exists

    second = exists("first.csv")
    first = exists("second.csv")

    if second:
        os.remove("first.csv")
    if first:
        os.remove("second.csv")
   
def deleteOjbectInDB():
    """Delete objects in database"""
    strategyResults.objects.all().delete()
    tradeResults.objects.all().delete()
    stocksTested.objects.all().delete()
    chartImage.objects.all().delete()

def getBodyContext(request, str):

    body_unicode = request.body.decode('utf-8')
    
    import ast
    d = ast.literal_eval(body_unicode)


    return (d[str])

def pushTradesIntoDatabase(closedTrades):



    tradeResults.objects.get_or_create(
        tradeid                         = str(int(closedTrades['tradeID']) - 1),
        stock                           = closedTrades['stock'],
        trade_complete                  = closedTrades['trade_complete'],
        date_of_pivot_high              = closedTrades['date_of_pivot_one'],
        date_of_pivot_low               = closedTrades['date_of_pivot_two'],
        price_of_pivot_high             = closedTrades['price_of_pivot_one'],
        price_of_pivot_low              = closedTrades['price_of_pivot_two'],
        date_pivot_high_snr_tested      = closedTrades['date_pivot_one_snr_tested'],
        price_pivot_high_snr_tested     = closedTrades['price_pivot_one_snr_tested'],
        date_entered_short              = closedTrades['date_entered_short'],
        price_entered_short             = closedTrades['price_entered_short'],
        date_closed_short               = closedTrades['date_closed_short'],
        price_closed_short              = closedTrades['price_closed_short'],
        high_close_mark                 = closedTrades['pivotOneCloseMark'],
        low_close_mark                  = closedTrades['pivotTwoCloseMark'],
        trade_result                    = closedTrades['trade_result'],
        pnl                             ="{:.2f}".format(closedTrades['price_entered_short'] - float(closedTrades['price_closed_short'])),
        rsi                             = closedTrades['rsi'],
        riskRewardRatio                 = closedTrades['riskRewardRatio'],
        risk = closedTrades['risk'],
        reward = closedTrades['reward'],


    )

def pushResultsIntoDatabase(results,length, largestWin, largestLost):

    if largestWin > 0:
        largestWin = '%.2f'%largestWin
    else:
        largestWin = 0
    
    if largestLost < 0:
        largestLost = '%.2f'%largestLost
    else:
        largestLost = 0
    
    
    strategyResults.objects.get_or_create(
        active          = results['active'],
        stock           = results['stock'],
        length          = length,
        total_open      = results['total_open'],
        total_close     = results['total_close'],
        total_won       = results['total_won'],
        total_lost      = results['total_lost'],
        pnl             = results['PnL'],
        strike_rate     = results['strike_rate'],
        largestWin      = largestWin,
        largestLost     = largestLost

    )

    return HttpResponse('backend homepage')

def allStockSymbolsInDB():

    stocks = stock.objects.all()

    """Convert into queryset"""
    querySet = stocks.values_list('symbol')
    stockSymbolsTuple = []
    for i in querySet:
        if i not in stockSymbolsTuple:
            stockSymbolsTuple.append(i)

    stockSymbols = []
    for each in stockSymbolsTuple:
        for k in each:
            stockSymbols.append(k)
    
def regex(str):

    number = r"\d+"
    string = r"^\w+"

    test_str = str

    matches = re.findall(string, test_str, re.MULTILINE)

    return(matches[0])

def organizeAllPnl(allTrades):

    singlePnl   = []

    for each in allTrades:
        for each2 in each:
            singlePnl.append('%.2f'%float(each2['pnl']))


    positivePnl = []
    nevativePnl = []

    for each in singlePnl:
        if float(each) > 0:
            positivePnl.append(float(each))
        elif float(each) <= 0:
            nevativePnl.append(float(each))

    return positivePnl, nevativePnl

def getAveragePnlWinAndLost(positivePnl,nevativePnl):

    avgWin      = 0
    avgLost     = 0

    if len(positivePnl) > 0:
        avgWin      = (sum(positivePnl) / len(positivePnl))

    if len(nevativePnl) > 0:
        avgLost     = (sum(nevativePnl) / len(nevativePnl))

    return avgWin, avgLost

def getPnlHighAndLow(positivePnl,nevativePnl):

    largestWin  = 0
    largestLost = 0

    if len(positivePnl) > 0:
        largestWin  = max(positivePnl)

    if len(nevativePnl) > 0:
        largestLost = min(nevativePnl)


    return largestWin, largestLost

def getTotalResults(allResults):

    open    = []
    closed  = []
    won     = []
    lost    = []
    pnl     = []
    wr      = []
    

    count = 0
    for trade in allResults:

        if trade['active'] == True:
            count += 1
            open.append(float(trade['total_open']))
            closed.append(float(trade['total_close']))
            won.append(float(trade['total_won']))
            lost.append(float(trade['total_lost']))
            pnl.append(float(trade['PnL']))
            wr.append(float(trade['strike_rate']))
            
    totalOpen   = sum(open)
    totalClosed = sum(closed)
    totalWon    = sum(won)
    totalLost   = sum(lost)
    totalPnl    = sum(pnl)
    if sum(wr) == 0:
        totalWr = 0
    else:
        totalWr     = sum(wr) / count


    return totalOpen, totalClosed, totalWon, totalLost, totalPnl, totalWr

def pushTotalResultsIntoDB(allTrades, totalOpen, totalClosed, totalWon, totalLost, totalPnl, totalWr, tested, longestTrade, shortestTrade, avgTrade, longestOneToTwo, shortestOneToTwo, avgOneToTwo, longestTwoToShort, shortestTwoToShort, avgTwoToShort):

    totalResults.objects.all().delete()

    # positivePnl, nevativePnl = organizeAllPnl(allTrades)
    # largestWin, largestLost = getPnlHighAndLow(positivePnl,nevativePnl)
    # avgWin, avgLost = getAveragePnlWinAndLost(positivePnl,nevativePnl)

    totalResults.objects.get_or_create(
        tested      = tested,
        totalOpen   = int(totalOpen),
        totalClosed = int(totalClosed),
        totalWon    = int(totalWon),
        totalLost   = int(totalLost),
        totalPnl    = '%.2f'%totalPnl,
        totalWr     = '%.2f'%totalWr,
        # largestWin  = '%.2f'%float(largestWin),
        # largestLost = '%.2f'%float(largestLost),
        # avgWin      = '%.2f'%float(avgWin),
        # avgLost     = '%.2f'%float(avgLost),
        longestTrade = '%.0f'%float(longestTrade),
        shortestTrade      = '%.0f'%float(shortestTrade),
        avgTrade     = '%.0f'%float(avgTrade),
        longestOneToTwo     = '%.0f'%float(longestOneToTwo),
        shortestOneToTwo     = '%.0f'%float(shortestOneToTwo),
        avgOneToTwo     = '%.0f'%float(avgOneToTwo),
        longestTwoToShort     = '%.0f'%float(longestTwoToShort),
        shortestTwoToShort     = '%.0f'%float(shortestTwoToShort),
        avgTwoToShort     = '%.0f'%float(avgTwoToShort),
    )

def convertChartDataIntoCSV(charts):
    # Convert each chart data into a df csv.
    for index, each in enumerate(charts):
        x = 0
        if len(each) > 0:
            for trade in each:


                reversedList = [trade['dates'][::-1], trade['open'][::-1],trade['high'][::-1],trade['low'][::-1],trade['close'][::-1]]
                df = pd.DataFrame (reversedList).transpose()
                df.columns = ['date', 'open', 'high', 'low', 'close']
                df.to_csv('C:\\Users\\rpere\\Desktop\\ABCD\\App\\main\\TempCsvs\\' + trade['tickerSymbol']  + '-' +  str(x + 1) + '.csv', index=False)
                x += 1

def removeFilesFromPreviousTest():

    # Delete any chart data from previous testing.
    for each in config.allCharts:
        file = exists(each)
        if file:
            os.remove(each)

    # Delete any data from previous testing.
    deleteOjbectInDB()

    # Delete chart images from previous testing.
    for filename in os.listdir('C:\\Users\\rpere\\Desktop\\ABCD\\App\\main\\main\\media\\media\\images'):

        os.remove(f'C:\\Users\\rpere\\Desktop\\ABCD\\App\\main\\media\\media\\images\\{filename}')

    # Delete chart images from previous testing.
    for filename in os.listdir('C:\\Users\\rpere\\Desktop\\ABCD\\App\\main\\TempCsvs'):

        os.remove(f'C:\\Users\\rpere\\Desktop\\ABCD\\App\\main\\TempCsvs\\{filename}')
    
    stocksTested.objects.all().delete()

def runTestOnEachStockGiven(request, selectedRunList):

    allResults  = []
    allTrades   = []
    allCharts   = []
   
    for each in selectedRunList:

        # Store names of stocks being tested for 'Run' display.
        stocksTested.objects.get_or_create(
            stock = each,
        )

        # Get a stocks data.
        stockName  = stock.objects.filter(symbol=each)


        # Convet stock data into a df csv.
        df  = stockNameIntoCSV(stockName)

 

        # Get user input settings from front end
        length, ticker, plBelowPh, PHtoPLLength, pLtoShortLength, marketType, strategy = getUserInput(request,each)

        # Run Engine
        strategyStatistics, allTrades = runBot(length, df, ticker, plBelowPh, PHtoPLLength, pLtoShortLength, marketType, strategy)

        # Collect Results
        # allCharts.append(chartData)
        # allTrades.append(closedTrades)
        # allResults.append(results)

        # x = 0
        # y = 0

        # if len(closedTrades) > 0:

        #     totalPNL, avgPNL, largestWin, largestLost, avgWin, avgLost = getTradeinfo(closedTrades)
        #     x = largestWin
        #     y = largestLost

        # # Push strategy results into database
        # pushResultsIntoDatabase(results, length, x,y)

        # # Push trades into database
        # for index, each in enumerate(closedTrades):
        #     pushTradesIntoDatabase(each)

        
        deleteTempfiles()

    return allResults, allTrades, allCharts

def getUserList(request, name):

    selectedRunList = getBodyContext(request, name)
    selectedRunList = selectedRunList.split(",")

    return selectedRunList

def getLengthsOfTrades(trades, firstDate, secondDate):

    allDays = []
    for each in trades:
        date_entered_short  = datetime.strptime(str(each[firstDate]), '%Y-%m-%d')
        date_closed_short   = datetime.strptime(str(each[secondDate]), '%Y-%m-%d')

        days = date_entered_short - date_closed_short
        allDays.append(abs(int(str(days.days))))
    longest    = 0
    shortest   = 0
    avg        = 0
    
    if len(allDays) > 0:
        longest    = max(allDays)
        shortest   = min(allDays)
        avg        = mean(allDays)

    return longest, shortest, avg

def getTradeinfo(trades):



    allPNL    = []
    wins      = []
    losses    = []

    for trade in trades:

        allPNL.append(float(trade['pnl']))

        if float(trade['pnl']) > 0:
            wins.append(float(trade['pnl']))
        if float(trade['pnl']) < 0:
            losses.append(float(trade['pnl']))


    totalPNL    = sum(allPNL)
    avgPNL      = mean(allPNL)
    largestWin  = max(allPNL)
    largestLost = min(allPNL)

    if len(wins) > 0:
        avgWin      = mean(wins)
    else:
        avgWin = 0
    if len(losses) > 0:
        avgLost     = mean(losses)
    else:
        avgLost = 0


    return totalPNL, avgPNL, largestWin, largestLost, avgWin, avgLost

def getTrades(stockName):

    trades = list(tradeResults.objects.filter(stock=stockName[0]).values())

    return trades

def pushDataIntoStockStatistics(stockName, totalPNL, avgPNL, largestWin, largestLost, avgWin,avgLost,longestTrade,shortestTrade,avgTrade):

    stockStatistics.objects.get_or_create(
        stock           = stockName[0],
        totalPnl        = '%.2f'%totalPNL,
        avgPnl          = '%.2f'%avgPNL,
        largestWin      = '%.2f'%largestWin,
        largestLost     = '%.2f'%largestLost,
        avgWin          = '%.2f'%avgWin,
        avgLost         = '%.2f'%avgLost,
        longestTrade    = longestTrade,
        shortestTrade   = shortestTrade,
        avgTrade        = '%.0f'%avgTrade,
    )

def getAmountTested(allResults):

    length = len(allResults)
    tested = 0
    noTest = 0

    for each in allResults:
        if each['active'] == True:
            tested += 1
        elif each['active'] == False:
            noTest += 1

    testedAndLength = str(tested) + '/' + str(length)

    return testedAndLength