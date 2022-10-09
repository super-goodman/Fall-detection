import threading
from SenseHat.ICM20948 import ICM20948
from time import sleep
import io
import time

class FallThread (threading.Thread):
   def __init__(self, threadID, name):
      threading.Thread.__init__(self)
      self.acc = ICM20948()
   def run(self):
      contG = 9.80665
      arr = []
      self.start = time.time()
      for i in range (800):
         x,y,z = self.acc.readAccclerometer()
         ax = ((2*16) / (2**13)) * x * contG
         ay = ((2*16) / (2**13)) * y * contG
         az = ((2*16) / (2**13)) * z * contG
         arr.append([ax, ay, az]) 
      print(time.time()-self.start)
      f = open("Data.txt","w")
      for j in range (800):
         toWrite = str(arr[j])
         toWrite = toWrite.replace('[','')
         toWrite = toWrite.replace(']','')
         f.write(toWrite)
         if j < 800:
            
            f.write(',\n')
      
      f.close()
      print ("writing finished!")
      
     # numpy.savetxt('textData.txt',arr,fmt='%s')

      #return arr
   
