from datetime import datetime, timedelta
import time

def setStartEndDate(date,daysBack):
    
    startDate = datetime.strptime(date, '%d/%m/%y') - timedelta(days=daysBack, hours=0)

    return startDate

def convertDatesIntoUnix(enteredEndDate, startDate):

    unixStartDate = time.mktime(startDate.timetuple())
    unixEndDate = time.mktime(datetime.strptime(enteredEndDate, '%d/%m/%y').timetuple())

    return unixStartDate, unixEndDate
