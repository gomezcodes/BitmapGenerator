import time as t
from datetime import datetime,date

def millis():

    return t.time()

def nonBlockingDelay(currentTime, timeOut):

    if ((currentTime + timeOut) < millis()):
        return True
    else:
        return False

def currentDate():
    now = datetime.now()
    dt_string = now.strftime("%B %d %Y %H:%M")

    return dt_string


