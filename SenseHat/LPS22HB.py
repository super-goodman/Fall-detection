from sense_hat import SenseHat
class LPS22HB(object): # Temp and humidity
    def __init__(self):
        self.pressure = 0 
        self.sense = SenseHat()
        self.sense.clear()
    #read Tempreture
    def readPressure(self):
        self.pressure = self.sense.get_pressure()
        print(self.pressure)
        return self.pressure
    

