from sense_hat import SenseHat
class ICM20948(object): # Temp and humidity
    def __init__(self):
        self.x = 0 
        self.y = 0 
        self.z = 0 
        self.acc = 0
        self.sense = SenseHat()
        self.sense.clear()
       
        
    #read Accclerometer
    def readAccclerometer(self):
        self.acc = self.sense.get_accelerometer_raw()
        self.x = self.acc["x"]
        self.y = self.acc["y"]
        self.z = self.acc["z"]
        self.x = round(self.x, 0)
        self.y = round(self.y, 0)
        self.z = round(self.z, 0)
        print("x={0}, y={1}, z={2}".format(self.x,self.y,self.z))
        return self.x,self.y,self.z
    



