
import csv
import os
import matplotlib.pyplot            as plt
import pandas                       as pd
import numpy                        as np
from stock.ultilities               import *
# from abcd_script.trading_bot.abcd.models.trade import Trade
from abcd_script.trading_bot.abcd.models.trade import Trade
from .models                        import activeTrades,savedLists, stock, stockStatistics, strategyResults, totalResults, tradeResults, chartImage, stocksTested
from django.http                    import HttpResponse
from .serializers                   import ActiveTradeSerializer,StockStatisticsSerializer, StrategyResultSerializer, TotalResultsSerializer, TradeResultSerializer, ChartImageSerializer, StocksTestedSerializer,SavedListsSerializer
from rest_framework                 import generics
from django.shortcuts               import redirect, render, redirect
from django.views.decorators.csrf   import csrf_exempt
from statistics                     import mean
import finnhub
from datetime import datetime, timedelta
import time
import pandas as pd
import time
from trade.views import createTrade


def CSVtoDatabase(file):

    for filename in os.listdir('../main\\CSV-2017-2021'):
        
        df = pd.read_csv(f'../main/CSV-2017-2021/{filename}', header=[0])
        df.columns = df.iloc[0] 
        df = df[1:]
        df = df.reset_index(drop=True)
        df.to_csv(filename,index=None)
        fhand = open(f'C:\\Users\\rpere\\OneDrive\\Desktop\\Code\\StockBotWeb\\main\\{filename}')
        reader = csv.reader(fhand)

        for row in reader:

            try:
                obj = stock.objects.create(date=row[0],open=row[1], close=row[2],high=row[3],low=row[4],adjClose=row[5], volume=row[6], symbol=regex(filename))
            except stock.DoesNotExist:
                obj = stock.objects.create(date=row[0],open=row[1], close=row[2],high=row[3],low=row[4],adjClose=row[5], volume=row[6], symbol=regex(filename))
                obj.save()

        fhand.close()
        os.remove(filename)

@csrf_exempt
def singleStockEngine(request):

    selectedRunList = getUserList(request, 'selectedRunList')

    removeFilesFromPreviousTest()

    allResults, allTrades, allCharts = runTestOnEachStockGiven(request, selectedRunList)

    convertChartDataIntoCSV(allCharts)

    totalOpen, totalClosed, totalWon, totalLost, totalPnl, totalWr = getTotalResults(allResults)

    tradesList = []
    for trade in allTrades:

        tradesList.append(trade)

    longestOneToTwo, shortestOneToTwo, avgOneToTwo = getLengthsOfTrades(tradesList, 'dateOfA','dateofB')
    longestTwoToShort, shortestTwoToShort, avgTwoToShort = getLengthsOfTrades(tradesList, 'dateofB','dateEnteredShort')
    # longestTrade, shortestTrade, avgTrade = getLengthsOfTrades(tradesList, 'dateEnteredShort','dateClosedShort')


    testedAndLength = getAmountTested(allResults)

    pushTotalResultsIntoDB(allTrades, totalOpen, totalClosed, totalWon, totalLost, totalPnl, totalWr, testedAndLength, 0, 0, 0, longestOneToTwo, shortestOneToTwo, avgOneToTwo, longestTwoToShort, shortestTwoToShort, avgTwoToShort)

    return HttpResponse('Hello BackEnd')

@csrf_exempt
def getTradeID(request):

    chartImage.objects.all().delete()

    stockName   = getBodyContext(request, 'stock')
    tradeID     = getBodyContext(request, 'tradeID') 
    tradeID     = str(int(tradeID) + 1)
    tradeID     = str(int(tradeID))
    df          = pd.read_csv ('C:\\Users\\rpere\\Desktop\\abcd\\abcd_local\\abcd_server\\App\\main\\TempCsvs\\' + stockName + '-' + tradeID + '.csv') 
    df          = pd.DataFrame(data=df)
    df.reset_index(inplace=True)
    df['date']  = pd.to_datetime(df.date, format='%Y-%m-%d')
    x           = np.arange(0,len(df))
    fig, ax     = plt.subplots(1, figsize=(12,6))

    for idx, val in df.iterrows():
        color = '#2CA453'
        if val['open'] > val['close']: color= '#F04730'
        plt.plot([x[idx], x[idx]], 
                [val['low'], val['high']], 
                color=color)
        plt.plot([x[idx], x[idx]-0.1], 
                [val['open'], val['open']], 
                color=color)
        plt.plot([x[idx], x[idx]+0.1], 
                [val['close'], val['close']], 
                color=color)

    fig.patch.set_facecolor('black')
    # ticks
    # plt.xticks(x[::1], df.date.dt.date[::1])
    ax.xaxis.set_tick_params(rotation=90)
    ax.set_facecolor('black')
    ax.tick_params(axis='x', colors='white')    #setting up X-axis tick color to red
    ax.tick_params(axis='y', colors='white')  #setting up Y-axis tick color to black
    ax.spines['left'].set_color('white')        # setting up Y-axis tick color to red
    ax.spines['bottom'].set_color('white')         #setting up above X-axis tick color to red

    # #  Top Close
    # plt.axhline(y=float(trade['topclose']),  color='red')

    # # # Support and Resistance
    # plt.axhline(y=float(trade['sr']),        color='black')

    # # # Bot Close
    # plt.axhline(y=float(trade['botclose']),  color='green')

    # grid
    ax.xaxis.grid(color='black', linestyle='dashed', which='both', alpha=0.1)
    
    # remove spines
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)

    # title
    plt.title( stockName + '-' + tradeID , fontsize=20, color= 'white')

    plt.savefig(f'C:\\Users\\rpere\\Desktop\\abcd\\abcd_local\\abcd_server\\App\\main\\main\\media\\media\\images\{stockName}-{tradeID}.png')

    image = ((f'C:\\Users\\rpere\\Desktop\\abcd\\abcd_local\\abcd_server\\App\\main\\main\\media\\media\\images\\{stockName}-{tradeID}.png'))

    chartImage.objects.get_or_create(
        image = image,

    )
    plt.close()

    return HttpResponse('Hello BackEnd')

@csrf_exempt
def newSavedList(request):

    listName = getBodyContext(request, 'listName')
    list = getBodyContext(request, 'list')
    list = list.split(",")

    for each in list:
        savedLists.objects.get_or_create(
            name    = listName,
            stock   = each,
        )


    return HttpResponse('Hello BackEnd')

@csrf_exempt
def deleteSavedList(request):

    list = getBodyContext(request, 'listName')
    list = list.split(",")



    for each in list:

        objects = savedLists.objects.filter(name=each)

        for each in objects:
            savedLists.objects.filter(id=each.id).delete()

    
    return HttpResponse('Hello BackEnd')

@csrf_exempt
def deleteItemsInList(request):

    listName = getBodyContext(request, 'listName')

    list = getBodyContext(request, 'names')
    list = list.split(",")

    for each in list:

        objects = savedLists.objects.filter(name=listName).filter(stock=each)

        for each in objects:
            savedLists.objects.filter(id=each.id).delete()


    return HttpResponse('Hello BackEnd')

@csrf_exempt
def deleteChartImage(request):

    chartImage.objects.all().delete()

    return HttpResponse('Hello BackEnd')

@csrf_exempt
def getStockStatistics(request):

    # stockStatistics.objects.all().delete()
   
    stockName = getUserList(request, 'stock')

    trades = getTrades(stockName)

    if len(trades) > 0:

        longestTrade, shortestTrade, avgTrade = getLengthsOfTrades(trades, 'date_entered_short','date_closed_short')

        totalPNL, avgPNL, largestWin, largestLost, avgWin, avgLost = getTradeinfo(trades)

        pushDataIntoStockStatistics(stockName, totalPNL, avgPNL, largestWin, largestLost, avgWin,avgLost, longestTrade, shortestTrade, avgTrade)

    return HttpResponse('Hello BackEnd')

@csrf_exempt
def getLiveData(request):

    tradesMade = []

    activeTrades.objects.all().delete()

    # Errors:  remove time stamp from dates from entire column
    allStockNames = [ 
      'ACBI','BDSI',  'BKEP',  'BKEPP', 'ALT', 'AACG', 'AAL', 'AAME', 'AAOI', 'AAON', 'AAPL', 'AATC', 'AAWW', 'ABCB', 'ABEO', 'ABIO','ABST', 'ABTX', 'ABUS','ACB', 'ACER', 'ACGL', 'ACGLO', 'ACHC', 'ACHV', 'ACIU', 'ACIW',
      'ACLS', 'ACMR', 'ACNB', 'ACOR', 'ACRS', 'ACRX', 'ACST', 'ACTG', 'ADAP', 'ADBE', 'ADES', 'ADI', 'ADMA', 'ADMP', 'ADP', 'ADSK', 'ADTN', 'ADUS', 'ADVM', 'ADXS', 'AEHL', 'AEHR', 'AEIS', 'AEMD', 'AEP', 
      'AERI', 'AESE', 'AEYE', 'AEZS', 'AFBI', 'AFMD', 'AGFS', 'AGIO', 'AGRX', 'AGTC', 'AGYS', 'AHPI', 'AIKI', 'AIMC', 'AINV', 'AIRG', 'AIRT', 'AKAM', 'AKBA', 'AKTS', 'AKTX', 'ALGN', 'ALGT', 'ALJJ', 'ALKS', 
      'ALLT', 'ALNY', 'ALOT', 'ALPN', 'ALPP', 'ALRM', 'ALRN', 'ALRS', 'ALTO', 'ALTR', 'ALYA', 'AMAT', 'AMBA', 'AMCX', 'AMD', 'AMED','AMEH', 'AMGN', 'AMKR', 'AMNB', 'AMOT', 'AMPH', 'AMRK', 'AMRN', 'AMRS', 
      'AMSC', 'AMSF', 'AMWD', 'AMZN', 'ANAB', 'ANAT', 'ANDE', 'ANGI', 'ANSS', 'ANTE', 'ANY', 'AOSL', 'APA', 'APDN', 'APEI', 'APEN', 'APLS', 'APOG', 'APPF', 'APPN', 'APPS', 'APTO', 'APVO',
      'APWC', 'AQB', 'AQMS', 'ARAV', 'ARAY', 'ARCB', 'ARCC', 'ARCT', 'AREC', 'ARGX', 'ARTNA', 'ASND', 'ASPU', 'ASTC', 'ASUR', 'ATEX', 'ATHE', 'ATLC', 
      'ATNI', 'ATOS', 'ATRC', 'ATRO', 'ATVI', 'ATXI', 'ATXS','AUB', 'AUBN', 'AUDC', 'AUPH', 'AUTO', 'AVAV', 'AVCT', 'AVDL', 'AVEO',
      'AVGO', 'AVGR', 'AVID', 'AVNW', 'AVT', 'AVTX', 'AVXL', 'AWH', 'AWRE', 'AXDX', 'AXGN', 'AXON', 'AXSM', 'AXTI', 'AY', 'AYRO', 'AYTU', 'AZN', 'AZPN', 'BAND',
      'BANF', 'BANFP', 'BANR', 'BANX', 'BATRK', 'BBBY', 'BBCP', 'BBGI', 'BBI', 'BBQ', 'BBSI', 'BCBP', 'BCDA', 'BCLI', 'BCML', 'BCOR', 'BCOV', 'BCPC', 'BCRX',
      'BCTX', 'BECN', 'BEEM', 'BELFA', 'BELFB', 'BFC', 'BFIN', 'BGCP', 'BGFV', 'BGNE', 'BHF', 'BIDU', 'BIIB', 'BIMI', 'BIOC', 'BIOL', 'BJRI', 'BKCC',
      'BKNG', 'BKSC', 'BKYI', 'BL', 'BLBD', 'BLCM', 'BLDP', 'BLFS', 'BLIN', 'BLKB', 'BLMN', 'BLNK', 'BLPH', 'BLRX', 'BLU', 'BLUE', 'BMRA',
      'BMRC', 'BMRN', 'BNFT', 'BNSO', 'BNTC', 'BOKF', 'BOMN', 'BOOM', 'BOSC', 'BOTJ', 'BOXL', 'BPMC', 'BPOP', 'BPOPM', 'BPRN', 'BPTH', 'BRCN', 'BRID', 'BRKL',
      'BRKR', 'BRQS', 'BSCM', 'BSCN', 'BSCO', 'BSCP', 'BSCQ', 'BSCR', 'BSET', 'BSGM', 'BSJM',
      'BSJN', 'BSJO', 'BSJP', 'BSQR', 'BSRR', 'BTB', 'BTCS', 'BTEC', 'BTX', 'BUSE', 'BVXV', 'BWEN', 'BWFG', 'BYFC', 'BYRN', 'BYSI', 'BZUN', 'CAAS', 'CAC', 'CACC',
      'CACG', 'CAKE', 'CALA', 'CALM', 'CAMP', 'CAMT', 'CAPR', 'CAR', 'CARA', 'CARE', 'CARG', 'CARV', 'CARZ', 'CASA', 'CASH', 'CASI', 'CASS', 'CASY', 'CATC', 'CATH',
      'CATY', 'CBAN', 'CBAT', 'CBAY', 'CBFV', 'CBIO', 'CBRL', 'CBSH', 'CBTX', 'CCBG', 'CCD', 'CCEP', 'CCLP', 'CCMP', 'CCNE', 'CCOI', 'CCRN', 'CCXI', 'CDC',
      'CDEV', 'CDK', 'CDL', 'CDMO', 'CDNA', 'CDNS', 'CDTX', 'CDW', 'CDXC', 'CDXS', 'CDZI', 'CECE', 'CELC', 'CELH', 'CEMI', 'CENT', 'CENTA', 'CENX', 'CERN', 'CERS',
      'CETX', 'CETXP', 'CEVA', 'CEY', 'CFA', 'CFBK', 'CFFI', 'CFFN', 'CFMS', 'CFO', 'CFRX', 'CG', 'CGBD', 'CGC', 'CGEN', 'CGNX', 'CGO', 'CGRN', 'CHCI', 'CHCO', 'CHDN',
      'CHEF', 'CHEK', 'CHKP', 'CHMG', 'CHNR', 'CHRS', 'CHRW', 'CHSCL', 'CHSCM', 'CHSCN', 'CHSCO', 'CHSCP', 'CHTR', 'CHUY', 'CHW', 'CHY', 'CIBR', 'CID', 'CIDM', 'CIGI',
      'CIL', 'CINF', 'CIVB', 'CIZ', 'CLBS', 'CLDX', 'CLIR', 'CLLS', 'CLPT', 'CLRB', 'CLRG', 'CLRO', 'CLSD', 'CLSK', 'CLSN', 'CLXT', 'CMCO', 'CMCSA', 'CMCT', 'CME',
      'CMPR', 'CMRX', 'CNCE', 'CNCR', 'CNDT', 'CNET', 'CNFR', 'CNOB', 'CNSL', 'CNTY', 'CNXN', 'COCP', 'CODA', 'CODX', 'COFS', 'COHR', 'COHU', 'COKE', 'COLB', 'COLL',
      'COLM', 'COMM', 'COMS', 'COMT', 'CONE', 'CONN', 'COOP', 'CORT', 'COST', 'COUP', 'COWN', 'CPHC', 'CPIX', 'CPLP', 'CPRT', 'CPRX', 'CPSH', 'CPSI', 'CPSS', 'CPTAG',
      'CPTAL', 'CRAI', 'CRBP', 'CRDF', 'CREG', 'CRESY', 'CREX', 'CRIS', 'CRMD', 'CRMT', 'CROX', 'CRSP', 'CRTO', 'CRUS', 'CRVL', 'CRVS', 'CRWS',
      'DBVT', 'DCOM', 'DCPH', 'DGICA', 'DGII', 'DGLY', 'DGRE', 'DGRS', 'DGRW', 'DHCNI', 'DIOD', 'DISCA', 'DISCB', 'DISCK', 'DISH', 'DJCO', 'DLHC', 'DLPN',
      'DLTH', 'DLTR', 'DMAC', 'DMLP', 'DMRC', 'DMTK', 'DNLI', 'DOGZ', 'DOOO', 'DORM', 'DOX', 'DRIO', 'DRRX', 'DRTT', 'DSGX', 'DSKE', 'DSWL', 'DTEA', 'DTST', 'DUOT',
      'DVY', 'DWAS', 'DWAT', 'DWPP', 'DWSN', 'DXCM', 'DYNT', 'DZSI', 'EA', 'EAST', 'EBAY', 'EBIX', 'EBMT', 'ECPG', 'EDAP', 'EDIT', 'EDSA', 'EDUC', 'EEFT', 'EEMA', 'EFAS',
      'EFOI', 'EGAN', 'EGBN', 'EGLE', 'EGRX', 'EMIF', 'EMKR', 'EML', 'EMXC', 'ENDP', 'ENG', 'ENLV', 'ENVB', 'ENZL', 'EPAY', 'EPIX', 'EPSN', 'EPZM', 'EQBK', 'EQIX',
      'EQRR', 'ERIC', 'ERIE', 'ERII', 'ERYP', 'ESBK', 'ESCA', 'ESEA', 'ESGD', 'ESGE', 'ESGR', 'ESGU', 'ESLT', 'ESPR', 'ESQ', 'ESSA', 'ETSY', 'EUFN', 'EVBG', 'EVFM',
      'EVO', 'EVOK', 'EVOL', 'EWBC', 'EWZS', 'EXAS', 'EXC', 'EXEL', 'EXLS', 'EXPD', 'EXPE', 'EXPO', 'EXTR', 'EYE', 'EYES', 'EYPT', 'EZPW', 'FAAR', 'FAB', 'FAD', 'FALN',
      'FANG', 'FANH', 'FARM', 'FARO', 'FAST', 'FAT', 'FATE', 'FB', 'FBIO', 'FBIOP', 'FBIZ', 'FBMS', 'FBNC', 'FBRX', 'FBZ', 'FCA', 'FCAL', 'FCAP', 'FCBC', 'FCCO', 'FCCY',
      'FCEF', 'FCEL', 'FCFS', 'FCNCA', 'FCRD', 'FCVT', 'FDBC', 'FDIV', 'FDT', 'FDTS', 'FDUS', 'FEIM', 'FELE', 'FEM', 'FEMB', 'FEMS', 'FENC', 'FEP', 'FEUZ', 'FEX',
      'FFBC', 'FFBW', 'FFHL', 'FFIC', 'FFIN', 'FFIV', 'FFNW', 'FFWM', 'FGBI', 'FGEN', 'FGF', 'FID', 'FINX', 'FISI', 'FISV', 'FITB', 'FITBI', 'FIVE', 'FIVN', 'FIXD',
      'FIZZ', 'FJP', 'FKU', 'FKWL', 'FLDM', 'FLEX', 'FLGT', 'FLIC', 'FLL', 'FLMN', 'FLNT', 'FLXS', 'FMAO', 'FMB', 'FMBH',
      'FMBI', 'FMHI', 'FMNB', 'FNCB', 'FNHC', 'FNK', 'FNKO', 'FNLC', 'FNWB', 'FNWD', 'FNX', 'FNY', 'FOLD', 'FONR', 'FORD', 'FORM', 'FORR', 'FORTY', 'FOSL', 'FOXF',
      'FPA', 'FPAY', 'FPXI', 'FRAF', 'FRBA', 'FRBK', 'FRGI', 'FRME', 'FRPH', 'FRPT', 'FRSX', 'FRTA', 'FSBW', 'FSFG', 'FSLR', 'FSTR', 'FSTX', 'FSV', 'FSZ', 'FTA',
      'FTAG', 'FTC', 'FTCS', 'FTEK', 'FTFT', 'FTGC', 'FTHI', 'FTLB', 'FTNT', 'FTSL', 'FTSM', 'FTXD', 'FTXG', 'FTXH', 'FTXL', 'FTXN', 'FTXO', 'FTXR', 'FULT',
      'FUNC', 'FUND', 'FUSB', 'FUV', 'FV', 'FVC', 'FVCB', 'FVE', 'FWBI', 'FWONA', 'FWP', 'FWRD', 'FXNC',
      'FYC', 'FYT', 'FYX', 'GAIA', 'GAIN', 'GALT', 'GASS', 'GBCI', 'GBDC', 'GBLI', 'GBOX', 'GBT', 'GCBC', 'GDEN', 'GDS', 'GECC', 'GEG', 'GENC', 'GENE',
      'GENY', 'GEOS', 'GERN', 'GGAL', 'GIFI', 'GIGM', 'GIII', 'GILD', 'GILT', 'GLAD', 'GLBS', 'GLBZ', 'GLDD', 'GLDI', 'GLG', 'GLMD', 'GLNG', 'GLPG',
      'GRBK', 'GREE', 'GRFS', 'GRID', 'GRMN', 'GROM', 'GROW', 'GRPN', 'GRVY', 'GSBC', 'GSIT', 'GSM', 'GT', 'GTHX', 'GTIM', 'GTYH', 'GURE', 'GVP', 'GWGH',
      'GWRS', 'GYRO', 'HA', 'HAFC', 'HAIN', 'HALL', 'HALO', 'HAS', 'HAYN', 'HBAN', 'HBCP', 'HBIO', 'HBMD', 'HBNC', 'HBP', 'HCCI', 'HCKT', 'HCM', 'HCSG',
      'HDSN', 'HEAR', 'HEES', 'HELE', 'HEPA', 'HEWG', 'HFBL', 'HFFG', 'HFWA', 'HGBL', 'HGEN', 'HGSH', 'HIBB', 'HIFS', 'HIHO', 'HIMX', 'HLNE', 'HMHC',
      'HMNF', 'HMST', 'HMTV', 'HNNA', 'HNRG', 'HOFT', 'HOLI', 'HOLX', 'HOMB', 'HON', 'HONE', 'HOPE', 'HOVNP', 'HQY', 'HROW', 'HRTX', 'HRZN', 'HSDT',
      'HTBK', 'HTBX', 'HTGM', 'HTHT', 'HTLD', 'HTLF', 'HUBG', 'HURC', 'HURN', 'HUSN', 'HVBC', 'HWBK', 'HWC', 'HWKN', 'HYXF', 'HYZD', 'HZNP', 'IAC', 'IART',
      'IBB', 'IBKR', 'IBOC', 'IBRX', 'IBTX', 'ICAD', 'ICCC', 'ICFI', 'ICHR', 'ICLK', 'ICLN', 'ICLR', 'ICMB', 'ICPT', 'ICUI', 'IDCC', 'IDEX', 'IDLB', 'IDRA',
      'IDXX', 'IEA', 'IEF', 'IEI', 'IEP', 'IESC', 'IGF', 'IGIB', 'IGOV', 'IGSB', 'III', 'IIN', 'IIVI', 'IJT', 'ILMN', 'IMBI', 'IMCV', 'IMGN', 'IMKTA',
      'IMMP', 'IMMR', 'IMOS', 'IMRN', 'IMTE', 'IMUX', 'IMV', 'IMXI', 'INBK', 'INCY', 'INDB', 'INDP', 'INDT', 'INDY', 'INFI', 'INFN', 'INFR', 'INGN', 'INM',
      'INO', 'INOD', 'INPX', 'INSE', 'INSG', 'INSM', 'INTC', 'INTG', 'INTU', 'INTZ', 'INVA', 'INVE', 'IONS', 'IOSP', 'IOVA', 'IPA', 'IPAR', 'IPDN', 'IPGP',
      'IPKW', 'IPWR', 'IRBT', 'IRCP', 'IRDM', 'IRIX', 'IRMD', 'IROQ', 'IRTC', 'IRWD', 'ISBC', 'ISEE', 'ISRG', 'ISSC', 'ISTB', 'ISTR', 'ISUN', 'ITCI',
      'ITI', 'ITIC', 'ITRI', 'ITRN', 'IUSB', 'IUSG', 'IUSV', 'IVAC', 'JAZZ', 'JBHT', 'JBLU', 'JBSS', 'JCS', 'JCTCF', 'JD', 'JJSF', 'JKHY', 'JNCE', 'JOUT',
      'JRJC', 'JRVR', 'JSM', 'JSMD', 'JSML', 'JVA', 'JYNT', 'KALA', 'KALU', 'KALV', 'KBWB', 'KBWD', 'KBWP', 'KBWR', 'KBWY', 'KDNY', 'KDP', 'KE', 'KELYA',
        'KEQU', 'KFFB', 'KFRC', 'KHC', 'KIDS', 'KINS', 'KIRK', 'KLAC', 'KLIC', 'KMDA', 'KMPH', 'KNDI', 'KNSL', 'KOPN', 'KOR', 'KOSS', 'KPTI', 'KRMA',
      'KRMD', 'KRNT', 'KRNY', 'KRYS', 'KSPN', 'KTCC', 'KTOS', 'KTRA', 'KURA', 'KVHI', 'KXIN', 'KZIA', 'LAKE', 'LAMR', 'LANC', 'LAND', 'LARK', 'LAUR', 'LAWS',
      'LBAI', 'LBC', 'LBRDA', 'LBRDK', 'LBTYA', 'LBTYB', 'LBTYK', 'LCNB', 'LCUT', 'LE', 'LECO', 'LEDS', 'LEE', 'LFMD', 'LFUS', 'LFVN', 'LGIH', 'LGND', 'LGO',
      'LHCG', 'LIFE', 'LILA', 'LILAK', 'LINC', 'LIND', 'LINK', 'LIQT', 'LITE', 'LIVE', 'LIVN', 'LIXT', 'LJPC', 'LKFN', 'LKQ', 'LLL', 'LLNW', 'LMAT', 'LMB',
      'LMBS', 'LMFA', 'LMNL', 'LMNR', 'LMST', 'LNDC', 'LNT', 'LNTH', 'LOAN', 'LOB', 'LOCO', 'LOGI', 'LOOP', 'LOPE', 'LPCN', 'LPLA', 'LPSN', 'LPTH', 'LPTX',
      'LQDT', 'LRCX', 'LRFC', 'LRGE', 'LRMR', 'LSBK', 'LSCC', 'LSTR', 'LSXMA', 'LSXMB', 'LSXMK', 'LTBR', 'LTRPA','LTRX', 'LULU', 'LUMO', 'LUNA',
      'LVHD', 'LVO', 'LWAY', 'LWLG', 'LX', 'LXRX', 'LYL', 'LYTS', 'MACK', 'MANH', 'MANT', 'MARA', 'MARK','MASI', 'MAT', 'MATW', 'MAYS', 'MBB',
      'MBCN', 'MBII', 'MBIN', 'MBIO', 'MBOT', 'MBRX', 'MBUU', 'MBWM', 'MCBC', 'MCEF', 'MCFT', 'MCHI', 'MCHP', 'MCHX', 'MCRB', 'MCRI', 'MDB', 'MDGL', 'MDGS',
      'MDIV', 'MDLZ', 'MDRX', 'MDVL', 'MDWD', 'MDXG', 'MEDP', 'MEDS', 'MEIP', 'MELI', 'MEOH', 'MERC', 'MESO', 'MFH', 'MFIN', 'MGI', 'MGIC', 'MGNI', 'MGPI',
      'MGRC', 'MGYR', 'MHLD', 'MICT', 'MIDD', 'MILN', 'MIME', 'MIND', 'MINDP', 'MITK', 'MKSI', 'MKTX', 'MLAB', 'MLCO', 'MLKN', 'MLVF', 'MMAT',
      'MMSI', 'MMYT', 'MNDO', 'MNDT', 'MNKD', 'MNMD', 'MNOV', 'MNRO', 'MNSB', 'MNST', 'MNTX', 'MODV', 'MOFG', 'MOMO', 'MORN', 'MOXC', 'MPAA', 'MRAM', 'MRBK',
      'MRCC', 'MRCY', 'MRIN', 'MRKR', 'MRLN', 'MRNS', 'MRSN', 'MRTX', 'MRUS', 'MRVL', 'MSEX', 'MSFT', 'MSTR', 'MSVB', 'MTBC', 'MTBCP', 'MTCH', 'MTEM', 'MTEX',
      'MTLS', 'MTP', 'MTRX', 'MTSI', 'MU', 'MULN', 'MVBF', 'MVIS', 'MYGN', 'MYMD', 'MYRG', 'MYSZ', 'NAII', 'NAKD', 'NAOV', 'NATH', 'NATI', 'NATR', 'NAVI', 'NBEV',
      'NBIX', 'NBN', 'NBRV', 'NBSE', 'NCBS', 'NCMI', 'NCNA', 'NCTY', 'NDAQ', 'NDLS', 'NDRA', 'NDSN', 'NEGG', 'NEO', 'NEOG', 'NEON', 'NEPH', 'NEPT', 'NERV', 'NESR',
      'NEWT', 'NEXT', 'NFBK', 'NFLX', 'NFTY', 'NH', 'NHTC', 'NICE', 'NICK', 'NISN', 'NKSH', 'NKTR', 'NLOK', 'NLTX', 'NMFC', 'NMIH', 'NMRK', 'NMTR', 'NNDM', 'NODK',
      'NOTV', 'NOVN', 'NRBO', 'NRC', 'NRIM', 'NSEC', 'NSIT', 'NSPR', 'NSSC', 'NSTG', 'NSYS', 'NTAP', 'NTCT', 'NTES', 'NTGR', 'NTIC', 'NTLA', 'NTNX', 'NTRA', 'NTRS',
      'NTWK', 'NUAN', 'NURO', 'NUVA', 'NUWE', 'NVAX', 'NVCN', 'NVCR', 'NVDA', 'NVEC', 'NVEE', 'NVFY', 'NVIV', 'NVMI', 'NWBI', 'NWE', 'NWFL', 'NWL', 'NWLI', 'NWPX',
      'NWS', 'NWSA', 'NXGN', 'NXPI', 'NXST', 'NXTD', 'NXTG', 'NXTP', 'NYMT', 'NYMTN', 'NYMX', 'OAS', 'OBAS', 'OBCI', 'OBLG', 'OBSV','OCC', 'OCFC', 'OCGN',
      'OCUL', 'OCUP', 'OCX', 'GLPI', 'GLRE', 'GLYC', 'GMAB', 'GMBL', 'GNCA', 'GNSS', 'GNTX', 'GNTY', 'GNUS', 'GOGL', 'GOGO', 'GOOD', 'GOOG', 'GOOGL', 'GPP', 'GPRE', 'GPRO',
      'ODFL', 'ODP', 'ODT', 'OEG', 'OESX', 'OFED', 'OFIX', 'OFLX', 'OFS', 'OIIM', 'OKTA', 'OLB', 'OLED', 'OLLI', 'OMAB', 'OMCL', 'OMER', 'OMEX', 'OMP',
      'OMQS', 'ON', 'ONB', 'ONCS', 'ONCT', 'ONCY', 'ONEQ', 'ONTX', 'ONVO', 'OPBK', 'OPCH', 'OPGN', 'OPHC', 'OPK', 'OPNT', 'OPOF', 'OPRX', 'OPTN',
      'ORGO', 'ORGS', 'ORLY', 'ORMP', 'ORRF', 'OSAT', 'OSBC', 'OSIS', 'OSPN', 'OSTK', 'OSUR', 'OSW', 'OTEX', 'OTIC', 'OTLK', 'OTRK', 'OTTR', 'OVBC',
      'OVID', 'OVLY', 'OXBR', 'OXLC', 'OXLCM', 'OXSQ', 'OZK', 'PAA', 'PAAS', 'PACB', 'PACW', 'PAGP', 'PAHC', 'PALI', 'PALT', 'PANL', 'PANW', 'PATI',
      'PATK', 'PAVM', 'PAYS', 'PAYX', 'PBCT', 'PBCTP', 'PBHC', 'PBIP', 'PBLA', 'PBPB', 'PBYI', 'PCAR', 'PCH', 'PCOM', 'PCRX', 'PCSB',
      'PCTI', 'PCTY', 'PCYG', 'PCYO', 'PDBC', 'PDCE', 'PDCO', 'PDEX', 'PDFS', 'PDLB', 'PDP', 'PDSB', 'PEBK', 'PEBO', 'PEGA', 'PENN', 'PEP', 'PERI',
      'PESI', 'PETQ', 'PETS', 'PETV', 'PETZ', 'PEY', 'PEZ', 'PFBC', 'PFC', 'PFF', 'PFG', 'PFI', 'PFIE', 'PFIN', 'PFIS', 'PFLT', 'PFM', 'PFMT', 'PFSW',
      'PFX', 'PGC', 'PGEN', 'PGJ', 'PHIO', 'PHO', 'PHUN', 'PI', 'PID', 'PIE', 'PINC', 'PIO', 'PIRS', 'PIXY', 'PIZ', 'PKBK', 'PKOH', 'PKW', 'PLAB', 'PLAY',
      'PLBC', 'PLCE', 'PLPC', 'PLSE', 'PLUG', 'PLUS', 'PLW', 'PLXP', 'PLXS', 'PLYA', 'PMCB', 'PMD', 'PME', 'PMTS', 'PNBK', 'PNFP', 'PNNT', 'PNQI', 'PNRG',
      'POAI', 'PODD', 'POLA', 'POOL', 'POWI', 'POWL', 'POWW', 'PPBI', 'PPBT', 'PPC', 'PPH', 'PPSI', 'PRAA', 'PRDO', 'PRFT', 'PRFZ', 'PRGS', 'PRIM', 'PROV',
      'PRPH', 'PRPO', 'PRQR', 'PRTA', 'PRTG',  'PRTK', 'PRTS', 'PSC', 'PSCC', 'PSCD', 'PSCE', 'PSCF', 'PSCH', 'PSCI', 'PSCM', 'PSCT', 'PSCU',
      'PSEC', 'PSET', 'PSHG', 'PSL', 'PSMT', 'PSTI', 'PSTV', 'PTC', 'PTCT', 'PTE', 'PTEN', 'PTF', 'PTGX', 'PTH', 'PTMN', 'PTNR', 'PTRS', 'PTSI', 'PUI', 'PVBC',
      'PWFL', 'PWOD', 'PXI', 'PXLW', 'PXS', 'PY', 'PYPL', 'PYR', 'PYZ', 'PZZA', 'QABA', 'QAT', 'QCLN', 'QCOM', 'QCRH', 'QDEL', 'QIPT', 'QIWI', 'QLGN', 'QLYS',
      'QMCO', 'QNRX', 'QNST', 'QQEW', 'QQQ', 'QQQX', 'QQXT', 'QRHC', 'QRTEA', 'QRTEB', 'QRVO', 'QTEC', 'QTNT', 'QTRX', 'QUBT', 'QUIK', 'QUMU', 'QURE', 'QYLD',
      'RADA', 'RAIL', 'RAND', 'RARE', 'RAVE', 'RBB', 'RBBN', 'RBCAA', 'RBCN', 'RCEL', 'RCII', 'RCKT', 'RCKY', 'RCM', 'RCMT', 'RCON', 'RCRT', 'RDCM',
      'RDFN', 'RDHL', 'RDI', 'RDIB', 'RDNT', 'RDUS', 'RDWR', 'REDU', 'REED', 'REFR', 'REG', 'REGI', 'REGN', 'REKR', 'RELL', 'REPH', 'RESN', 'RETA', 'RETO',
      'RFDI', 'RFEM', 'RFEU', 'RFIL', 'RGCO', 'RGEN', 'RGLD', 'RGLS', 'RGNX', 'RGP', 'RIBT', 'RICK', 'RIGL', 'RILY', 'RING', 'RIOT', 'RKDA', 'RLMD',
      'RMBS', 'RMCF', 'RMNI', 'RMR', 'RMTI', 'RNDB', 'RNDM', 'RNDV', 'RNEM', 'RNLC', 'RNMC', 'RNRG', 'RNSC', 'RNST', 'RNWK', 'ROCC', 'ROCK', 'ROIC', 'ROKU',
      'ROLL', 'ROST', 'RPD', 'RRGB', 'RRR', 'RSLS', 'RSSS', 'RTH', 'RUN', 'RUSHA', 'RUSHB', 'RUTH', 'RVNC', 'RVSB', 'RWLK', 'RYAAY', 'RYTM', 'RZLT', 'SABR',
      'SAFM', 'SAFT', 'SAGE', 'SAIA', 'SAL', 'SALM', 'SAMG', 'SANM', 'SANW', 'SASR', 'SATS', 'SAVA', 'SBAC', 'SBCF', 'SBET', 'SBFG', 'SBGI', 'SBLK',
      'SBNY', 'SBRA', 'SBSI', 'SBT', 'SBUX', 'SCHL', 'SCHN', 'SCKT', 'SCOR', 'SCPH', 'SCSC', 'SCVL', 'SCWX', 'SCYX', 'SCZ', 'SDG', 'SDVY', 'SECO', 'SEDG',
      'SEED', 'SEEL', 'SEIC', 'SELB', 'SELF', 'SENEA', 'SESN', 'SEVN', 'SFBC', 'SFIX', 'SFM', 'SFNC', 'SFST', 'SGA', 'SGBX', 'SGC', 'SGEN',
      'SGH', 'SGLB', 'SGMA', 'SGMO', 'SGMS', 'SGRP', 'SGRY', 'SHBI', 'SHEN', 'SHIP', 'SHOO', 'SHV', 'SHY', 'SHYF', 'SIEB', 'SIEN', 'SIFY', 'SIGA', 'SIGI',
      'SILC', 'SIMO', 'SINO', 'SINT', 'SIOX', 'SISI', 'SIVB', 'SKOR', 'SKYW', 'SKYY', 'SLAB', 'SLGN', 'SLM', 'SLMBP', 'SLNG', 'SLNH', 'SLNO', 'SLP', 'SLQD',
      'SLRC', 'SLRX', 'SLS', 'SLVO', 'SMBC', 'SMBK', 'SMCI', 'SMCP', 'SMED', 'SMH', 'SMID', 'SMIT', 'SMLR', 'SMMF', 'SMMT', 'SMPL', 'SMSI', 'SMTC', 'SMTI', 'SNBR', 'SNCR',
      'SND', 'SNDX', 'SNES', 'SNEX', 'SNFCA', 'SNGX', 'SNLN', 'SNOA', 'SNPS', 'SNSR', 'SNT', 'SNY', 'SOCL', 'SOHO', 'SOHOB', 'SOHOO', 'SOHU', 'SONN', 'SOTK',
      'SOXX', 'SP', 'SPCB', 'SPI', 'SPLK', 'SPNE', 'SPNS', 'SPOK', 'SPPI', 'SPRO', 'SPSC', 'SPTN', 'SPWH', 'SPWR', 'SQLV', 'SQQQ', 'SRAX', 'SRCE', 'SRCL', 'SRDX',
      'SRET', 'SREV', 'SRGA', 'SRNE', 'SRPT', 'SRRA', 'SRTS', 'SSB', 'SSBI', 'SSKN', 'SSNC', 'SSNT', 'SSP', 'SSSS', 'SSTI', 'SSYS', 'STAA', 'STAB', 'STAF', 'STBA',
      'STCN', 'STFC', 'STGW', 'STKL', 'STKS', 'STLD', 'STRA', 'STRL', 'STRS', 'STRT', 'STX', 'SUMR', 'SUNS', 'SUNW', 'SUPN', 'SUSB', 'SUSC', 'SVC', 'SVRA',
      'SVVC', 'SWBI', 'SWIR','SWKS', 'SYBT', 'SYBX', 'SYNA', 'SYNH', 'SYNL', 'SYPR', 'SYRS', 'TA', 'TACO', 'TACT', 'TAIT', 'TANH', 'TANNI', 'TANNL', 'TANNZ',
      'TAOP', 'TARA', 'TAST', 'TATT', 'TAYD', 'TBBK', 'TBK', 'TBNK', 'TBPH', 'TCBI', 'TCBK', 'TCFC', 'TCMD', 'TCOM', 'TCON', 'TCPC', 'TCX', 'TDIV', 'TEAM', 'TECH',
      'TEDU', 'TENX', 'TER', 'TESS', 'TFSL', 'TGA', 'TGLS', 'TGTX', 'THFF', 'THMO', 'THRM', 'THTX', 'TILE', 'TIPT', 'TITN', 'TLT', 'TMDI', 'TMUS', 'TNDM', 'TNXP',
      'TOMZ', 'TOUR', 'TOWN', 'TPIC', 'TPST', 'TQQQ', 'TREE', 'TRHC', 'TRIB', 'TRIP', 'TRMB', 'TRMK', 'TRNS', 'TROW', 'TRS', 'TRST', 'TRUE', 'TRUP', 'TRVG', 'TRVN',
      'TSBK', 'TSC', 'TSCO', 'TSEM', 'TSLA', 'TSRI', 'TTD', 'TTEC', 'TTEK', 'TTGT', 'TTMI', 'TTNP', 'TTOO', 'TTSH', 'TTWO', 'TUR', 'TURN', 'TUSA', 'TUSK', 'TVTX',
      'TVTY', 'TWIN', 'TWNK', 'TWOU', 'TXMD', 'TXN', 'TXRH', 'TYME', 'TZOO', 'UAL', 'UBCP', 'UBFO', 'UBOH', 'UBSI', 'UCBI', 'UCTT', 'UEIC', 'UEPS', 'UFCS', 'UFPI',
      'UFPT', 'UG', 'UHAL', 'UIHC', 'ULBI', 'ULH', 'ULTA', 'UMBF', 'UMPQ', 'UNAM', 'UNB', 'UNIT', 'UNTY', 'UONE', 'UONEK', 'UPLD', 'URBN', 'URGN',
      'USAK', 'USAP', 'USAU', 'USEG', 'USIG', 'USIO', 'USLB', 'USLM', 'USMC', 'UTHR', 'UTMD', 'UTSI', 'UVSP', 'VABK', 'VALU','VBIV', 'VBLT', 'VBTX',
      'VC', 'VCEL', 'VCIT', 'VCLT', 'VCSH', 'VCYT', 'VECO', 'VEON', 'VERB', 'VERI', 'VERO', 'VERU', 'VEV', 'VG', 'VGIT', 'VGLT', 'VGSH', 'VIA', 'VIAC', 'VIASP', 'VIAV',
      'VICR', 'VIGI', 'VIRC', 'VIRT', 'VIRX', 'VISL', 'VIVE', 'VIVO', 'VJET', 'VKTX', 'VQS', 'VREX', 'VRME', 'VRNA', 'VRNS', 'VRNT', 'VRRM', 'VSAT', 'VSEC',
      'VSMV', 'VSTM', 'VTC', 'VTGN', 'VTHR', 'VTNR', 'VTSI', 'VTWG', 'VTWV', 'VUZI', 'VWOB', 'VWTR', 'VXRT', 'VXUS',
      'WATT', 'WBA', 'WDAY', 'WDC', 'WEN', 'WERN', 'WETF', 'WFCF', 'WHF', 'WHLM', 'WHLR', 'WHLRD', 'WINT', 'WIRE', 'WKHS', 'WLDN', 'WNEB', 'WPRT', 'WSBC',
      'WSBF', 'WSC', 'WSFS', 'WTBA', 'WTER', 'WTFC', 'WTRH', 'WVE', 'WVFC', 'WVVI', 'WVVIP', 'WWD', 'WYNN', 'XEL', 'XELB', 'XENT', 'XFOR', 'XLNX', 'XNCR',
      'XOMA', 'XRAY', 'XTLB', 'YLDE', 'YMTX', 'YNDX', 'YTRA', 'YVR', 'YY', 'Z', 'ZBRA', 'ZEAL', 'ZION', 'ZIONO', 'ZKIN', 'ZNGA', 'ZSAN', 'ZUMZ', 'ZYNE', 'ZYXI']

    def getDF(stock, i):

        # Get current date
        date_time_str = '06/07/22'
        today = datetime.strptime(date_time_str, "%d/%m/%y")

        tomsDate = today + timedelta(days=1)
        tomsDate, sep, tail = str(tomsDate).partition(' ')

        # Get start date
        date_time_obj = datetime.strptime(date_time_str, '%d/%m/%y') - timedelta(days=310, hours=0)

        # Convert start, current date into unix
        unixStartDate = time.mktime(date_time_obj.timetuple())
        unixEndDate = time.mktime(datetime.strptime(date_time_str, '%d/%m/%y').timetuple())

        # Access finnhub
        finnhub_client = finnhub.Client(api_key="cc5aa82ad3i2vhf81cfg")

        # Get stock candles data
        res = finnhub_client.stock_candles(stock, 'D', int(unixStartDate), int(unixEndDate))

        # Convert data into pandas df.
        df = pd.DataFrame(res)

        # Rename Columns
        df = df.rename(columns={"c": "Close", "h": "High", "l": "Low", "o": "Open", "v": "volume", "t": "Date"})
    
        # Convert unix time into date format.
        df['Date'] = pd.to_datetime(df['Date'], unit='s')

        dates = []
        for each in df['Date']:
            each = str(each)
            each, sep, tail = each.partition(' ')
            dates.append(each)
        df['Date'] = dates

        # Add columns
        df['Symbol'] = stock
        df['Adj Close'] = 1.1
        selectedRunList = [stock]

        # Sort df
        df = df[['Date', 'Open', 'High','Low','Close', 'Adj Close', 'Symbol']]


        df.loc[len(df.index)] = [tomsDate, 0, 0, 0, 0, 1,stock] 

        if(df.shape[0] < 40):
            print('DF is not long enough')

        elif(df.shape[0] >= 40):
            removeFilesFromPreviousTest ()
            allResults, allTrades, allCharts = run(request, selectedRunList, df)
            print(i, allResults)
        

            allTrades.append(allResults)

    def sto(df):
        csv = df.to_csv(index=False)
        df["Date"] = pd.to_datetime(df["Date"], format='%Y-%m-%d')
        df['Date'].dt.strftime('%Y-%m-%d')
        with open('readme.csv', 'x') as f:
            f.write(csv)
        df = pd.read_csv('C:/Users/rpere/Desktop/abcd/abcd_local/abcd_server/main/readme.csv')
        df.to_csv('output.csv', index=False)
        return df

    def run(request, selectedRunList, pdf):
        allResults  = []
        allTrades   = []
        allCharts   = []
        for each in selectedRunList:
      
            df  = sto(pdf)
            length, ticker, plBelowPh, PHtoPLLength, pLtoShortLength, marketType, strategy = getUserInput(request,each)
            # print(df)
            openTrades, closedTrades, results, chartData = runBot(length, df, ticker, plBelowPh, PHtoPLLength, pLtoShortLength, marketType, strategy)

        
            for each in closedTrades:
                
                createTrade(each)

                # activeTrades.objects.get_or_create(
                #     tradeid = each['id'],
                #     date_of_pivot_high  = each['date_of_pivot_high'],
                #     date_of_pivot_low  = each['date_of_pivot_low'],
                #     price_of_pivot_high  = each['price_of_pivot_high'],
                #     price_of_pivot_low  = each['price_of_pivot_low'],
                #     date_pivot_high_snr_tested  = each['date_pivot_high_snr_tested'], 
                #     price_pivot_high_snr_tested  = each['price_pivot_high_snr_tested'],
                #     date_entered_short  = each['date_entered_short'],
                #     price_entered_short  = each['price_entered_short'],
                #     high_close_mark  = each['high_close_mark'],
                #     low_close_mark  = each['low_close_mark'],
                #     symbol = each['symbol'],
                #     activePrice = each['activePrice'],
                #     tradeType   = each['tradeType'],
                #     durationOfTrade = each['durationOfTrade'],
                #     ohlc = each['ohlc'],
                # )

            allCharts.append(chartData)
            allTrades.append(closedTrades)
            allResults.append(results)

            deleteTempfiles()
        return allResults, allTrades, allCharts

    counter = 0

    def func():
        for each in range(counter-60, counter-1):
            getDF(allStockNames[each], each)
            if allStockNames[each] == 'ZYXI':
                return True

        return False
    getDF('TGA', 1)

    return HttpResponse('Hello BackEnd')


    timeNow = 0
    while True:
        counter += 1
        timeNow += 1
        if timeNow == 60:
            print('60 seceonds have passed')
            timeNow = 0
            x = func()
            if x == True:
                counter = 0
        print('Timer: ',counter)
        time.sleep(1)


class AllModels(generics.ListCreateAPIView):
    queryset            = strategyResults.objects.all()
    serializer_class    = StrategyResultSerializer

class SingleModel(generics.RetrieveUpdateDestroyAPIView):
    queryset            = strategyResults.objects.all()
    serializer_class    = StrategyResultSerializer

class tradeResultModels(generics.ListCreateAPIView):
    queryset            = tradeResults.objects.all()
    serializer_class    = TradeResultSerializer

class chartImageModels(generics.ListCreateAPIView):
    queryset            = chartImage.objects.all()
    serializer_class    = ChartImageSerializer

class totalResultsModels(generics.ListCreateAPIView):
    queryset            = totalResults.objects.all()
    serializer_class    = TotalResultsSerializer

class stocksTestedModels(generics.ListCreateAPIView):
    queryset            = stocksTested.objects.all()
    serializer_class    = StocksTestedSerializer

class savedListsTestedModels(generics.ListCreateAPIView):
    queryset            = savedLists.objects.all()
    serializer_class    = SavedListsSerializer

class stockStatisticsModels(generics.ListCreateAPIView):
    queryset            = stockStatistics.objects.all()
    serializer_class    = StockStatisticsSerializer


class activeTradesModels(generics.ListCreateAPIView):
    queryset            = activeTrades.objects.all()
    serializer_class    = ActiveTradeSerializer








 # 'FCUV'  'FAB', 'FAD', 'ABVC', 'FTRI' 'USOI''VSDA', 'BLBX','ATNF', 'KELYB' 'PAVMW', 

#  Can scan 60 in 20 seconds. 
#  So 1min can scan 180