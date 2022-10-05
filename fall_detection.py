from ast import For, While
from SenseHat.SHTC3 import SHTC3
from SenseHat.LPS22HB import LPS22HB
from SenseHat.ICM20948 import ICM20948
from SenseHat.LEDMatrix import LEDMatrix
from SenseHat.PiThread import PiThread
import time 

if __name__ == "__main__":

    shtc3 = SHTC3()
    shtc3.readTemp()
    shtc3.readHumi()

    lps22hb = LPS22HB()
    lps22hb.readPressure()
   
    icm20948 = ICM20948()
   # for i in range(100):
   #     icm20948.readAccclerometer()
    ledMatrix = LEDMatrix()
    displayContent = ""
    displayContent = "T: " + str(shtc3.readTemp()) + " H: " + str(shtc3.readHumi()) + " P: " + str(lps22hb.readPressure())
    ledMatrix.displayStr(displayContent)
    """
    try:
      while True:
       do_something()
    except KeyboardInterrupt:
      pass
    """
    
    exitFlag = 0
    def print_time(threadName, delay, counter):
     while counter:
      if exitFlag:
         threadName.exit()
      time.sleep(delay)
      print ("%s: %s" % (threadName, time.ctime(time.time())))
      counter -= 1

    # Create new threads
    thread1 = PiThread(1, "Thread-1", 1)
    thread2 = PiThread(2, "Thread-2", 2)

    # Start new Threads
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
    print ("Exiting Main Thread")