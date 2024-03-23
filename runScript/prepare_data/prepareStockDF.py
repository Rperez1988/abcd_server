import pandas as pd


def organizeEditAndSortDF(stock,df):

    # Rename Columns
    df = df.rename(columns={"c": "Close", "h": "High", "l": "Low", "o": "Open", "v": "Volume", "t": "Date"})

    # Convert unix time into date format.
    # df['Date'] = pd.to_datetime(df['Date'], unit='s')

    dates = []
    for each in df['Date']:
        each = str(each)
        each, sep, tail = each.partition(' ')
        dates.append(each)
    df['Date'] = dates

    # # Add columns
    df['Symbol'] = stock
    df['Adj Close'] = 1.1
    stockNames = [stock]

    # # Sort df
    df = df[['Date', 'Open', 'High','Low','Close', 'Adj Close', 'Volume','Symbol']]

    return df, stockNames
