import threading
from SenseHat.ICM20948 import ICM20948

class FallThread (threading.Thread):
   def __init__(self, threadID, name):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      
   def run(self):
      print ("Starting " + self.name)
      icm20948 = ICM20948()
      print ("Exiting " + self.name)
   
