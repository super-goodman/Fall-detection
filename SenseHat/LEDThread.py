import threading
from LEDMatrix import LEDMatrix
from SHTC3 import SHTC3
from LPS22HB import LPS22HB


class LEDThread (threading.Thread):
   def __init__(self, threadID, name):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
   
      
   def run(self):
      print ("Starting " + self.name)
      shtc3 = SHTC3()
      shtc3.readTemp()
      shtc3.readHumi()

      lps22hb = LPS22HB()
      lps22hb.readPressure()
      
      ledMatrix = LEDMatrix.LEDMatrix()
      displayContent = ""
      displayContent = "T: " + str(shtc3.readTemp()) + " H: " + str(shtc3.readHumi()) + " P: " + str(lps22hb.readPressure())
      ledMatrix.displayStr(displayContent)
      print ("Exiting " + self.name)
   
