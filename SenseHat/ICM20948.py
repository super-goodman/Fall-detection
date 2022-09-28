
from typing_extensions import Self


class ICM20948(object): # Temp and humidity
    def __init__(self):
        self.x = 0 
        self.y = 0 
        self.z = 0 
        
    #read Accclerometer
    def readAccclerometer(self):
        #self.temp = sensehat.readTemp()
        print("readAccclerometer")
        return self.x,self.y,self.z
    

