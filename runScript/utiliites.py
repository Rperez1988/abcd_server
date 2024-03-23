import pandas as pd
from stock.ultilities import *
from trade.views import createTrade
import pandas as pd
import sys
sys.path.append('../')
from runScript.prepare_data.prepareData import prepareData
from abcd_script.trading_bot.cerebro.run_cerebro import runCerebro

def runTradingBot(request, sym):

    symbol, settingsName, market, pivotLength, rrr, sAndR, maxAtoBLength, maxBtoCLength, maxCtoDLength, entryRSI, abnormalPriceJump, pivotSteepness, aBelowB, startDate, endDate = getUserInput(request)
  
    settings: dict = {

        'settingsName': settingsName,
        'market': market,
        'pivotLength': pivotLength,
        'rrr': rrr,
        's&r': sAndR,
        'maxAtoBLength': maxAtoBLength,
        'maxBtoCLength': maxBtoCLength,
        'maxCtoDLength': maxCtoDLength,
        'entryRSI': entryRSI,
        'abnormalPriceJump': abnormalPriceJump,
        'pivotSteepness': pivotSteepness,
        'aBelowB': aBelowB,
        'inRestrictionArea': 'inRestrictionArea',
    }
            
    df, stockNames = prepareData(sym, startDate, endDate)

    if df is None:

        return 

    else:
        if doesDFHaveEnoughData(stockNames,df):
            
            allResults  = []
            allTrades   = []

            for each in stockNames:

                # df = convertDFtoCSV(df)

                df.to_csv('second.csv', index=False)
        
                totalStatistics, allTrades = runCerebro(df, sym,'C:/Users/rpere/Desktop/abcd/abcd_local/abcd_server/second.csv', settings)
        
            for each in allTrades:
                createTrade(each)

            # deleteTempfiles()

def doesDFHaveEnoughData(name, df):

    if(df.shape[0] < 40):
        print(name[0], 'DF is not long enough')
        return False
    
    elif(df.shape[0] >= 40):

        return True

# def convertDFtoCSV(df):

#     deleteTempfiles()

    # df["Date"] = pd.to_datetime(df["Date"], format='%Y-%m-%d')

    # df['Date'].dt.strftime('%Y-%m-%d')

    # csv = df.to_csv(index=False)

    # with open('first.csv', 'x') as f:
    #     f.write(csv)
    
    # df = pd.read_csv('C:/Users/rpere/Desktop/abcd/abcd_local/abcd_server/first.csv', index=False)

    # df.to_csv('second.csv', index=False)

    # Save the DataFrame 'df' directly to 'first.csv'
    # csv = df.to_csv('first.csv', index=False)

    # with open('first.csv', 'x') as f:
    #     f.write(csv)


    # return df

     # Save the DataFrame 'df' directly to 'first.csv'
    df.to_csv('second.csv', index=False)

    # df = pd.read_csv('C:/Users/rpere/Desktop/abcd/abcd_local/abcd_server/second.csv')

    # return df

def getUserInput(request):

    symbol = getBodyContext(request, 'symbol')
    settingsName = getBodyContext(request, 'settingsName')
    market= getBodyContext(request, 'market')
    pivotLength= getBodyContext(request, 'pivotLength')
    rrr= getBodyContext(request, 'rrr')
    sAndr= getBodyContext(request, 'sAndr')
    maxAtoBLength= getBodyContext(request, 'maxAtoBLength')
    maxBtoCLength= getBodyContext(request, 'maxBtoCLength')
    maxCtoDLength= getBodyContext(request, 'maxCtoDLength')
    entryRSI= getBodyContext(request, 'entryRSI')
    abnormalPriceJump= getBodyContext(request, 'abnormalPriceJump')
    pivotSteepness= getBodyContext(request, 'pivotSteepness')
    aBelowB= getBodyContext(request, 'aBelowB')
    startDate = getBodyContext(request, 'startDate')
    endDate = getBodyContext(request, 'endDate')
    inRestrictionArea= getBodyContext(request, 'inRestrictionArea')
    # barsFromBack= getBodyContext(request, 'barsFromBack')

    return (
        symbol,
        settingsName,
        market, 
        pivotLength, 
        rrr, 
        sAndr, 
        maxAtoBLength, 
        maxBtoCLength, 
        maxCtoDLength, 
        entryRSI, 
        abnormalPriceJump, 
        pivotSteepness,
        aBelowB,
        startDate,
        endDate)

