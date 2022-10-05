import threading
import time

exitFlag = 0

class PiThread (threading.Thread):
   def __init__(self, threadID, name, counter):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.counter = counter
   def run(self):
      print ("Starting " + self.name)
      self.print_time(self.name, self.counter, 5)
      print ("Exiting " + self.name)
   
   
   def print_time(self, threadName, delay, counter):
      while counter:
         if exitFlag:
            threadName.exit()
         time.sleep(delay)
         print ("%s: %s" % (threadName, time.ctime(time.time())))
         counter -= 1