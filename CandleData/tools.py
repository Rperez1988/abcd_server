import requests
import pandas as pd
from .models import *

def get_today_candle_data(output_size, ticker):

    api_key = 'PXHDZ1B7PB2HZGHS'
    output_size = output_size
    ticker = ticker
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

    for index, row in df.iterrows():
        if str(row.name) > '2024-01-25':
            df.drop(index, inplace=True)
        elif str(row.name) <= '2024-01-25':
            break

    # print(df[0])
    x = {

        'symbol': ticker,
        'date': df.index[0],
        'open': df.iloc[0].open,
        'close': df.iloc[0].close,
        'high': df.iloc[0].high,
        'low': df.iloc[0].close,
        'volume': df.iloc[0].volume,
    }


    return x

def get_all_db_candle_symbols():

    # CHECK ALL CANDLE SYMBOLS IN DB AND GET
    unique_symbols_objects = Candle.objects.values('symbol').distinct()
    unique_symbols = []

    for each in unique_symbols_objects:
        unique_symbols.append(each['symbol'])

    return unique_symbols
