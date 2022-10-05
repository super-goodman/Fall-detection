from sense_hat import SenseHat
class LPS22HB(object):
    def __init__(self):
        self.pressure = 0 
        self.sense = SenseHat()
        self.sense.clear()
    #read Pressure
    def readPressure(self):
        self.pressure = round(self.sense.get_pressure(),1)
        print(self.pressure)
        return self.pressure
    

