from runScript.prepare_data.setTestingDates import setStartEndDate
from runScript.prepare_data.setTestingDates import convertDatesIntoUnix
from runScript.prepare_data.getFinnHubbLiveData import getFinnHubStockDate
from runScript.prepare_data.prepareStockDF import organizeEditAndSortDF
from datetime import datetime, timedelta
import time


def prepareData(symbol, entered_start_date, entered_end_date):


    formatted_end_date = datetime.strptime(entered_end_date, '%Y-%m-%dT%H:%M:%S.%fZ')
    formatted_start_date = datetime.strptime(entered_start_date, '%Y-%m-%dT%H:%M:%S.%fZ')

    days_between = (formatted_end_date - formatted_start_date).days
    
    string_formatted_end_date = formatted_end_date.strftime('%d/%m/%y')
    formatted_start_date_date = datetime.strptime(string_formatted_end_date, '%d/%m/%y') - timedelta(days=days_between, hours=0)

    unixStartDate = time.mktime(formatted_start_date_date.timetuple())
    unixEndDate = time.mktime(datetime.strptime(string_formatted_end_date, '%d/%m/%y').timetuple())

    stockDataDF = getFinnHubStockDate(symbol, unixStartDate, unixEndDate)

    if stockDataDF is None:
        print(symbol, 'is empty')
        return stockDataDF, symbol

    else:


        stockDataDF, stockName = organizeEditAndSortDF(symbol,stockDataDF)

        return stockDataDF, stockName
