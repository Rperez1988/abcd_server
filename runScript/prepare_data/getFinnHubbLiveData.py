import finnhub
import pandas as pd

def getFinnHubStockDate(stocks, unixStartDate,unixEndDate):

    finnhub_client = finnhub.Client(api_key="cdm8ut2ad3ibbock69lgcdm8ut2ad3ibbock69m0")    
    res = finnhub_client.stock_candles(stocks, 'D', int(unixStartDate), int(unixEndDate))
    # res = finnhub_client.crypto_candles(stocks, 'D', int(unixStartDate), int(unixEndDate))

    try:
        df = pd.DataFrame(res)
        return df

    except:
        print(stocks, "ERROR: No Finnhub Data Was Returned")
 

