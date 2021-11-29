import time as t

def millis():

    return t.time()

def nonBlockingDelay(currentTime, timeOut):

    if ((currentTime + timeOut) < millis()):
        return True
    else:
        return False

