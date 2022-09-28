
class LPS22HB(object): # Temp and humidity
    def __init__(self):
        self.pressure = 0 
        
    #read Tempreture
    def readPressure(self):
        #self.temp = sensehat.readTemp()
        print("readPressure")
        return self.pressure
    

