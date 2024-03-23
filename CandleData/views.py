from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import pandas as pd
from .models import *
from rest_framework import generics
from .serializers import *
import csv
import requests
from CandleData.tools import *
from django.db import transaction

def check_last_date(all_symbols):
    
    for each in all_symbols:

        candles = Candle.objects.filter(symbol=each)

        # Convert the queryset to a list of dictionaries
        candles_data = candles.values()

        # # Create a Pandas DataFrame from the list of dictionaries
        candles_df = pd.DataFrame(candles_data)

        print(candles_df.iloc[0]['symbol'],candles_df.iloc[-1]['candle_date'])

    return HttpResponse('check_last_date')

def all_symbols_scanned(request):

    unique_symbols = Candle.objects.values('symbol').distinct()
    for each in unique_symbols:
        print(each)
    # BYON 5442
    return HttpResponse('get_index')

def update_today_candle_data(request):

    all_symbols = get_all_db_candle_symbols()
    
    # all_symbols = all_symbols[9700:]
    failed = {}
    
    for each in all_symbols:  
        try:
            candle = get_today_candle_data('compact',each)
            try:
                # Attempt to get the existing record
                candle = Candle.objects.get(symbol=candle['symbol'], candle_date=candle['date'])
                # The record exists
                print("Record exists:", candle)
            except Candle.DoesNotExist:
                # The record does not exist
                print("Update Candle: ", candle)

                Candle.objects.update_or_create(
                    symbol = candle['symbol'],
                    candle_date = candle['date'],
                    candle_open = candle['open'],
                    candle_high = candle['high'],
                    candle_low = candle['low'],
                    candle_close = candle['close'],
                    candle_volume = candle['volume'],
                )
        except Exception as e:
            print(e)
            failed[each] = e

    return HttpResponse('update_today_candle_data')

@csrf_exempt
def erase_candle_data(request):


    Candle.objects.all().delete()


    return HttpResponse('Erased')

def get_single_symbol_candles(request):

    api_key = 'PXHDZ1B7PB2HZGHS'
    output_size = 'full'
    ticker = 'AAPL'
    timeframe = 'TIME_SERIES_DAILY'

    # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    url = f'https://www.alphavantage.co/query?function={timeframe}&symbol={ticker}&outputsize={output_size}&apikey={api_key}'
    r = requests.get(url)
    data = r.json()

    symbol = data['Meta Data']['2. Symbol']
    data = data['Time Series (Daily)']

    # Convert to DataFrame
    df = pd.DataFrame({date: pd.Series(data[date]) for date in data})

    # Transpose the DataFrame
    df = df.T

    # Convert columns to numeric (optional, if needed)
    df = df.apply(pd.to_numeric, errors='coerce')

    # Rename columns to remove numbers and dots
    df = df.rename(columns=lambda x: x.split(' ')[-1])

    for date, row in df.iterrows():
        # Check if the record already exists
        existing_candle = Candle.objects.filter(symbol=symbol, candle_date=date).first()

        if existing_candle:
            # Update the existing record
            existing_candle.candle_open = row['open']
            existing_candle.candle_high = row['high']
            existing_candle.candle_low = row['low']
            existing_candle.candle_close = row['close']
            existing_candle.candle_volume = row['volume']
            existing_candle.save()
        else:
            # Create a new record
            Candle.objects.create(
                symbol=symbol,
                candle_date=date,
                candle_open=row['open'],
                candle_high=row['high'],
                candle_low=row['low'],
                candle_close=row['close'],
                candle_volume=row['volume']
            )

    return HttpResponse('get_single_symbol_candles')

@csrf_exempt
def get_ticker_symbols(request):

    

    # api_key = 'PXHDZ1B7PB2HZGHS'

    # # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    # CSV_URL = 'https://www.alphavantage.co/query?function=LISTING_STATUS&apikey=PXHDZ1B7PB2HZGHS'

    # with requests.Session() as s:
    #     download = s.get(CSV_URL)
    #     decoded_content = download.content.decode('utf-8')
    #     cr = csv.reader(decoded_content.splitlines(), delimiter=',')
    #     my_list = list(cr)
    #     for row in my_list:
    #         # print(row[0])
    #         if(row[0] != 'symbol'):
    #             SymbolInfo.objects.update_or_create(
    #                 symbol = row[0],
    #                 name = row[1],
    #                 exchange = row[2],
    #                 assetType = row[3],
    #                 ipoDate = row[4],
    #                 delistingDate = row[5],
    #                 status = row[6],
    #             )
        
    return HttpResponse("Symbols")

@csrf_exempt
def delete_all_ticker_symbols(request):

    SymbolInfo.objects.all().delete()
    return HttpResponse('Erased')

# GET ALL CANDLES FOR ALL SYMBOLS
@csrf_exempt
def get_all_symbol_candles(request):

    all_symbols = list(SymbolInfo.objects.all())

    failed = {}
    
    for index, ticker_ in enumerate(all_symbols):
  
        if index >= 1545:
            try: 

                api_key = 'PXHDZ1B7PB2HZGHS'
                output_size = 'full'
                ticker = ticker_.symbol
                timeframe = 'TIME_SERIES_DAILY'

                # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
                url = f'https://www.alphavantage.co/query?function={timeframe}&symbol={ticker}&outputsize={output_size}&apikey={api_key}'
                r = requests.get(url)
                data = r.json()

                symbol = data['Meta Data']['2. Symbol']
                data = data['Time Series (Daily)']

                # Convert to DataFrame
                df = pd.DataFrame({date: pd.Series(data[date]) for date in data})

                # Transpose the DataFrame
                df = df.T

                # Convert columns to numeric (optional, if needed)
                df = df.apply(pd.to_numeric, errors='coerce')

                # Rename columns to remove numbers and dots
                df = df.rename(columns=lambda x: x.split(' ')[-1])

                print(ticker, df.index[0],len(df))

                for date, row in df.iterrows():

                    # Check if the record already exists
                    existing_candle = Candle.objects.filter(symbol=symbol, candle_date=date).first()

                    if existing_candle:
                        # Update the existing record
                        existing_candle.candle_open = row['open']
                        existing_candle.candle_high = row['high']
                        existing_candle.candle_low = row['low']
                        existing_candle.candle_close = row['close']
                        existing_candle.candle_volume = row['volume']
                        existing_candle.save()
                    else:
                        # Create a new record
                        Candle.objects.create(
                            symbol=symbol,
                            candle_date=date,
                            candle_open=row['open'],
                            candle_high=row['high'],
                            candle_low=row['low'],
                            candle_close=row['close'],
                            candle_volume=row['volume']
                        )


            except Exception as e:
                failed[ticker] = e
                print(ticker, e)

                print(failed)

      
    
    # print(failed)
    return HttpResponse("Call")

# Check length
def check_all_symbols_in_db(request):

    # All alpha vantage symbols
    all_symbols = list(SymbolInfo.objects.all())
    
    # Symbols and its candles that are in db
    unique_symbols = list(Candle.objects.values('symbol').distinct())



    print(len(unique_symbols), unique_symbols[-1])
 


    return HttpResponse("check_all_symbols_in_db") 
from uuid import UUID
def getBodyContext(request, str):

    body_unicode = request.body.decode('utf-8')
    
    import ast
    d = ast.literal_eval(body_unicode)
    


    return (d[str])



@csrf_exempt
def selected_candles(request):

    try: 
        candles = getBodyContext(request, 'candles')
        trade_id = getBodyContext(request, 'trade_id')
        symbol = getBodyContext(request, 'symbol')

        print(symbol)

        with transaction.atomic():
            all_symbol_candles = list(Candle.objects.filter(symbol=symbol))
            SelectedCandles.objects.all().delete()
            
            selected_candles_to_create = [
                SelectedCandles(
                    trade_id=trade_id,
                    symbol=candle.symbol, 
                    candle_date=candle.candle_date,
                    candle_open=candle.candle_open,
                    candle_high=candle.candle_high,
                    candle_low=candle.candle_low,
                    candle_close=candle.candle_close,
                    candle_volume=candle.candle_volume,
                )
                for candle in all_symbol_candles
            ]
            
          
            SelectedCandles.objects.bulk_create(selected_candles_to_create)

    
            # ==========================================
            candles_queryset = list(Candle.objects.filter(id__in=candles))

    except Exception as e:
        print(e)
        return HttpResponse('candles')
    return HttpResponse('candles')

class Selected_Candles_API(generics.ListAPIView):
    queryset            = SelectedCandles.objects.all()
    serializer_class    = SelectedCandlesAPI

class CandleModels(generics.ListCreateAPIView):
    queryset            = Candle.objects.all()
    serializer_class    = CandleSerializer

class SymbolModels(generics.ListCreateAPIView):
    queryset            = SymbolInfo.objects.all()
    serializer_class    = SymbolInfoSerializer