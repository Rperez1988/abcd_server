import finnhub
import pandas as pd

def getFinnHubStockDate(stocks, unixStartDate,unixEndDate):

    # finnhub_client = finnhub.Client(api_key="cdm8ut2ad3ibbock69lgcdm8ut2ad3ibbock69m0")  
    finnhub_client = finnhub.Client(api_key="clkbuv9r01qso7g5jrc0clkbuv9r01qso7g5jrcg")    
    # res = finnhub_client.stock_candles(stocks, 'D', int(unixStartDate), int(unixEndDate))
    print(finnhub_client.stock_candles('AAPL', 'D', 1590988249, 1591852249))


    
    # res = finnhub_client.crypto_candles(stocks, 'D', int(unixStartDate), int(unixEndDate))

    # try:
    #     df = pd.DataFrame(res)
    #     return df

    # except:
    #     print(stocks, "ERROR: No Finnhub Data Was Returned")
 

