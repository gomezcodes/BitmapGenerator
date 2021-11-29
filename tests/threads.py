import threading
import time

def doThis():
    print("This is a thread")
    while (not dead):
        pass

dead = False

ourThread = threading.Thread(target=doThis) 
ourThread.start()

print (threading.active_count())
print (threading.enumerate())
print (ourThread.is_alive())



input( "Enter to stops")
dead = True

time.sleep(0.1)
print (ourThread.is_alive())


