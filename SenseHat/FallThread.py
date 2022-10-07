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
     
      arr = numpy.empty(2400, dtype = str)
      for i in range (2400):
         x,y,z = ICM20948.readAccclerometer()
         arr[i] = str(x)+','+str(y)+','+str(z)+','
         sleep(0.005)
      print ("Exiting " + self.name)
      
      f = open("testData.txt", "x")
      f.close()
      f = open("testData.txt", "a")
      for j in range (2400):
          f.write(arr[j])
      f.close()

      #return arr
   
