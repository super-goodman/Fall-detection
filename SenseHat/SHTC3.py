from sense_hat import SenseHat
class SHTC3(object): # Temp and humidity
    def __init__(self):
        self.temp = 0
        self.humi = 0  
        self.temp2 = 0
        self.sense = SenseHat()
        self.sense.clear()
    #read Tempreture
    def readTemp(self):
        self.temp = self.sense.get_temperature()
        self.temp2 = self.sense.get_temperature_from_pressure()
        print(self.temp)
        return self.temp
    
    #read humidity
    def readHumi(self):
        self.humi = self.sense.get_humidity()    
        print(self.humi)
        return self.humi

