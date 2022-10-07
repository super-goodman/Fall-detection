import threading
from SenseHat.ICM20948 import ICM20948
import numpy 
from time import sleep

class FallThread (threading.Thread):
   def __init__(self, threadID, name):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      
   def run(self):
      print ("Starting " + self.name)
     
      arr = numpy.empty(2400, dtype = "S20")
      for i in range (24):
         acc = ICM20948()
         x,y,z = acc.readAccclerometer()
         arr[i] = x + "," + y + "," + z + ","
         sleep(0.005)
      print ("Exiting " + self.name + arr[15])
      
      f1 = open("testData.txt", "x")
      f1.close()
      f2 = open("testData.txt", "a")
      for j in range (24):
          f2.write(arr[j])
      f2.close()

      #return arr
   
