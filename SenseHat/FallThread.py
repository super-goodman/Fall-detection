import threading
from SenseHat.ICM20948 import ICM20948
import numpy 
from time import sleep
import io

class FallThread (threading.Thread):
   def __init__(self, threadID, name):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      
   def run(self):
      print ("Starting " + self.name)
      contG = 9.80665
      arr = []
      for i in range (96):
         acc = ICM20948()
         x,y,z = acc.readAccclerometer()
         ax = ((2*16) / (2**13)) * x * contG
         ay = ((2*16) / (2**13)) * y * contG
         az = ((2*16) / (2**13)) * z * contG
         arr.append([ax, ay, az]) 
         sleep(0.005)
      print ("Exiting " + self.name)
      
      f = open("testData.txt","w")
      for j in range (96):
         f.write(str(arr[j]))
         if j < 96:
            
            f.write(',\n')
      
      
      
     # numpy.savetxt('textData.txt',arr,fmt='%s')

      #return arr
   
