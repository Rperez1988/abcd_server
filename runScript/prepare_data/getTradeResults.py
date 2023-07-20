import sys
sys.path.append('../')


# def getTradeResults(request, allStockNames):

#     customDate, todaysDate, tomorrowsDate = getCurrentDate('06/07/22')

#     unixStartDate, unixEndDate = startEndDatesToUnix(customDate,1000)

#     df = getFinnHubStockDate(allStockNames, unixStartDate, unixEndDate)

#     df, stockNames = organizeEditAndSortDF(allStockNames,df,tomorrowsDate)

#     if doesDFHaveEnoughData(df):
        
#         allResults  = []
#         allTrades   = []
#         allCharts   = []

#         for each in stockNames:

#             df = convertDFtoCSV(df)

#             length, ticker, plBelowPh, PHtoPLLength, pLtoShortLength, marketType, strategy = getUserInput(request,each)
            
            
#             openTrades, closedTrades, results, chartData, allTrades = runBot(length, df, ticker, plBelowPh, PHtoPLLength, pLtoShortLength, marketType, strategy)
    
#         allTrades.append(allResults)
