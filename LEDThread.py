import threading
from SenseHat.LEDMatrix import LEDMatrix
from SenseHat.SHTC3 import SHTC3
from SenseHat.LPS22HB import LPS22HB


class LEDThread (threading.Thread):
   def __init__(self, threadID, name):
      threading.Thread.__init__(self)
      self.shtc3 = SHTC3()
      self.lps22hb = LPS22HB()
      self.ledMatrix = LEDMatrix()
      
   def run(self):

      self.shtc3.readTemp()
      self.shtc3.readHumi() 
      self.lps22hb.readPressure()
      displayContent = "T: " + str(self.shtc3.readTemp()) + " H: " + str(self.shtc3.readHumi()) + " P: " + str(lps22hb.readPressure())
      self.ledMatrix.displayStr(displayContent)
   
