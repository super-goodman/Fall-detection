from sense_hat import SenseHat
class SHTC3(object): # Temp and humidity
    def __init__(self):
        self.temp = 0
        self.humi = 0  
        sense=SenseHat()
    #read Tempreture
    def readTemp(self):
        self.temp = sense.temp
        print(self.temp)
        return self.temp
    
    #read humidity
    def readHumi(self):
        print(123213)
        #self.temp = sensehat.readTemp()
        print("readHumi")
        return self.humi

