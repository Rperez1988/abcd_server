from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from CandleData.models import Candle
import pandas as pd
from abcd_script.trading_bot.cerebro.run_cerebro import runCerebro
import os
from runScript.prepare_data.prepareStockDF import organizeEditAndSortDF
from datetime import date, timedelta, datetime
from trade.models import all_trades
from access_trades.views import seperate_trades_by_bc, create_bc_peformances, create_cd_peformances
from all_patterns.views import *
from all_patterns.models import *
from django.db.models import Count
from CandleData.models import *

from RunStrategy.tools import *

@csrf_exempt
def remove_duplicate_entries(request):

    symbols = list(Candle.objects.values('symbol').distinct())

    # duplicate_instances = Candle.objects.values('candle_date', 'symbol').annotate(count=Count('id')).filter(count__gt=1)

    for symbol_entry in symbols:
        symbol_to_check = symbol_entry['symbol']
        duplicate_instances_for_symbol = Candle.objects.filter(symbol=symbol_to_check).values('candle_date').annotate(count=Count('id')).filter(count__gt=1)
        print(symbol_to_check)
        # Iterate over the duplicates and decide which to keep and which to remove
        for duplicate in duplicate_instances_for_symbol:
            candle_date_to_keep = duplicate['candle_date']

            # Get the first instance for a specific combination of 'candle_date' and 'symbol'
            instance_to_keep = Candle.objects.filter(candle_date=candle_date_to_keep, symbol=symbol_to_check).order_by('id').first()

            # Get all duplicate instances and exclude the first one
            instances_to_delete = Candle.objects.filter(candle_date=candle_date_to_keep, symbol=symbol_to_check).exclude(id=instance_to_keep.id)

            # Delete the duplicate instances
            instances_to_delete.delete()
    return HttpResponse('remove duplicates')

@csrf_exempt
def scan_single_symbols(request):

    # CREATE TEMP FILE PATH TO STORE CSV FOR BACKTRADER TO ACCESS.
    file_path = 'C:/Users/rpere/Desktop/abcd/abcd_local/abcd_server/tempcsv.csv'

    # RETRIEVE CANDLE DATA
    # data = list(Candle.objects.all())
    # five_years_ago = date.today() - timedelta(days=5 * 365)
    # data = Candle.objects.filter(candle_date__range=[five_years_ago, date.today()])

    # SCRIPT START, AND END DATE
    start_date, end_date = get_dates()

    # GET CANDLES BETWEEN DATES.
    data = Candle.objects.filter(candle_date__range=(start_date, end_date), symbol='AGQ')

    # 2018-01-03

    df, uuid_strings = prepare_candle_date(data)
    uuid_strings.append('0')
    df['Candle_ID'] = uuid_strings

    # BACKTRADER PARAMS
    settings: dict = {

        'candle_ids' :uuid_strings,
        'settingsName': uuid_strings,
        'market': 'market',
        'pivotLength': 1,
        'rrr': 'rrr',
        's&r': 'sAndR',
        'maxAtoBLength': 'maxAtoBLength',
        'maxBtoCLength': 'maxBtoCLength',
        'maxCtoDLength': 'maxCtoDLength',
        'entryRSI': 'entryRSI',
        'abnormalPriceJump': 'abnormalPriceJump',
        'pivotSteepness': 'pivotSteepness',
        'aBelowB': 'aBelowB',
        'inRestrictionArea': 'inRestrictionArea',

    }
  
    # GET ALL SYMBOLS IN DB
    pattern_a_symbols = Pattern_A.objects.values_list('trade_symbol', flat=True).distinct()

    pattern_A = []
    pattern_AB = []
    pattern_ABC = []
    pattern_ABCD = []
    
    # GATHER PATTERNS
    # for each in list(pattern_a_symbols):

    #     pattern_A = list(Pattern_A.objects.filter(trade_symbol=each))
    #     pattern_AB = list(Pattern_AB.objects.filter(trade_symbol=each))
    #     pattern_ABC = list(Pattern_ABC.objects.filter(trade_symbol=each))
    #     pattern_ABCD = list(Pattern_ABCD.objects.filter(trade_symbol=each))

    pattern_A = []
    pattern_AB = []
    pattern_ABC = []
    pattern_ABCD = []

    
    abcd_patterns, abc_patterns, ab_patterns, a_patterns = runCerebro(df, 'AGQ', file_path, settings, pattern_A, pattern_AB, pattern_ABC, pattern_ABCD, True, len(df))

    # print(df)           
    # print(len(abcd_patterns))
    # print(len(abc_patterns))
    # print(len(ab_patterns))
    # print(len(a_patterns))

    create_patterns_models(
        abcd_patterns,
        abc_patterns,
        ab_patterns,
        a_patterns   
    )

    # DELETE TEMP CSV FILE
    if os.path.exists(file_path):
        os.remove(file_path)

    return HttpResponse('RUN SCRIPT') 

def scan_all_symbols(request):

    symbols = list(Candle.objects.values('symbol').distinct())

    symbols = symbols[4737:]

    full_scan = True

    # CREATE TEMP FILE PATH TO STORE CSV FOR BACKTRADER TO ACCESS.
    file_path = 'C:/Users/rpere/Desktop/abcd/abcd_local/abcd_server/tempcsv.csv'
    

    for each in symbols:

    
        ticker = each['symbol']
        start_date, end_date = get_dates()

        # GET CANDLES BETWEEN DATES.
        data = Candle.objects.filter(candle_date__range=(start_date, end_date), symbol=ticker)

        df, uuid_strings = prepare_candle_date(data)
        df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d')  # Convert 'Date' column to datetime
        start_date = pd.to_datetime('01/01/2018', format='%m/%d/%Y')
        df = df[df['Date'] >= start_date].copy()
        df['Date'] = df['Date'].dt.strftime('%Y-%m-%d')

        # BACKTRADER PARAMS
        settings: dict = {

            'candle_ids' :uuid_strings[::-1],
            'settingsName': uuid_strings[::-1],
            'market': 'market',
            'pivotLength': 1,
            'rrr': 'rrr',
            's&r': 'sAndR',
            'maxAtoBLength': 'maxAtoBLength',
            'maxBtoCLength': 'maxBtoCLength',
            'maxCtoDLength': 'maxCtoDLength',
            'entryRSI': 'entryRSI',
            'abnormalPriceJump': 'abnormalPriceJump',
            'pivotSteepness': 'pivotSteepness',
            'aBelowB': 'aBelowB',
            'inRestrictionArea': 'inRestrictionArea',

        }

        pattern_A = list(Pattern_A.objects.filter(trade_symbol=ticker))
        pattern_AB = list(Pattern_AB.objects.filter(trade_symbol=ticker))
        pattern_ABC = list(Pattern_ABC.objects.filter(trade_symbol=ticker))
        pattern_ABCD = list(Pattern_ABCD.objects.filter(trade_symbol=ticker))

        try:

            # # RUN SCRIPT
            abcd_patterns, abc_patterns, ab_patterns, a_patterns = runCerebro(df, ticker, file_path, settings, pattern_A, pattern_AB, pattern_ABC, pattern_ABCD, full_scan, len(df))
        except Exception as e:
            print(e)
        
        print(ticker,'::',len(abcd_patterns))
        create_patterns_models(
            abcd_patterns,
            abc_patterns,
            ab_patterns,
            a_patterns    
        )

        # DELETE TEMP CSV FILE
        if os.path.exists(file_path):
            os.remove(file_path)


    
    return HttpResponse('RUN SCRIPT') 
