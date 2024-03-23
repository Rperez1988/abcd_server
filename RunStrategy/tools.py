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

def convert_data_into_pandas_df(data):

        df = pd.DataFrame([c.__dict__ for c in data])

       
        
        all_candle_ids = df['candle_id'].tolist()
        uuid_strings = [str(uuid_obj) for uuid_obj in all_candle_ids]
        df = df.drop(['_state', 'id',], axis=1)
        df.rename(columns={
        'candle_close': 'Close',
        'candle_high': 'High',
        'candle_low': 'Low',
        'candle_open': 'Open',
        'candle_date': 'Date',
        'candle_volume': 'Volume',
        }, inplace=True)
        df = df[['Date', 'Open', 'High','Low','Close', 'Volume']]


        # CREATE TEMP CSV FOR BACKTRADER
        
        df['Adj. Close'] = 1
        # print(df)
        df.to_csv('tempcsv.csv', columns=['Date', 'Open', 'High', 'Low', 'Close', 'Adj. Close','Volume'], index=False)

        return uuid_strings, df

def get_dates():
    # DEFINE START DATE FOR SCRIPT.
    start_date = date(2018, 1, 1)

    # Calculate the end date (5 years after the start date)

    # end_date = date(2024, 1, 12)
    # Get today's date
    today_date = datetime.now().date()

    # Subtract one day from today's date
    # end_date = today_date - timedelta(days=1)

    return start_date, today_date

def prepare_candle_date(data):
    # PREPARE CANDLE DATA
    uuid_strings, df = convert_data_into_pandas_df(data)

    # ADD DUMMY ROW TO CANDLE DATA
    last_date = str(df.iloc[-1]['Date'])
    original_datetime = datetime.strptime(last_date, '%Y-%m-%d')
    new_datetime = original_datetime + timedelta(days=1)
    new_date = new_datetime.strftime('%Y-%m-%d')
    new_row = {'Date': new_date, 'Open': 1, 'High': 1, 'Low': 1, 'Close': 1, 'Volume': 1}
    df.loc[len(df)] = new_row
    df['Date'] = pd.to_datetime(df['Date'])
    df = df.sort_values(by='Date', ascending=False).reset_index(drop=True)
    df = df[::-1]
    df['Date'] = df['Date'].dt.strftime('%Y-%m-%d')

    return df, uuid_strings