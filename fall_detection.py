from ast import For, While
from SenseHat.SHTC3 import SHTC3
from SenseHat.LPS22HB import LPS22HB
from SenseHat.ICM20948 import ICM20948
from SenseHat.LEDMatrix import LEDMatrix
from SenseHat.FallThread import FallThread
from SenseHat.LEDThread import LEDThread


if __name__ == "__main__":
    '''
    shtc3 = SHTC3()
    shtc3.readTemp()
    shtc3.readHumi()

    lps22hb = LPS22HB()
    lps22hb.readPressure()
    '''
  
   # for i in range(100):
   #     icm20948.readAccclerometer()
    
    """
    try:
      while True:
       do_something()
    except KeyboardInterrupt:
      pass
    """
    

    # Create new threads
    thread1 = FallThread(1, "Thread-1")
    thread2 = LEDThread(2, "Thread-2")

    # Start new Threads
    thread1.start()
    thread2.start()
  # thread1.join()
  # thread2.join()
    print ("Exiting Main Thread")