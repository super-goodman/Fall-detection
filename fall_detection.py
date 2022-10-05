from ast import For, While
from SenseHat.SHTC3 import SHTC3
from SenseHat.LPS22HB import LPS22HB
from SenseHat.ICM20948 import ICM20948
from SenseHat.LEDMatrix import LEDMatrix

if __name__ == "__main__":

    shtc3 = SHTC3()
    shtc3.readTemp()
    shtc3.readHumi()

    lps22hb = LPS22HB()
    lps22hb.readPressure()
   
    icm20948 = ICM20948()
   # for i in range(100):
   #     icm20948.readAccclerometer()
   
    LEDMatrix.displayStr("Hello there!")
