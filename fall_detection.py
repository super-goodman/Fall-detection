from ast import For, While
from SenseHat.SHTC3 import SHTC3
from SenseHat.LPS22HB import LPS22HB
from SenseHat.ICM20948 import ICM20948
from SenseHat.LEDMatrix import LEDMatrix
from FallThread import FallThread
from LEDThread import LEDThread


if __name__ == "__main__":

    # Create new threads
    thread1 = FallThread(1, "Thread-1")
    thread2 = LEDThread(2, "Thread-2")

    # Start new Threads
    thread1.start()
    thread2.start()
    print ("Exiting Main Thread")