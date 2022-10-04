from sense_hat import SenseHat
class ICM20948(object): # Temp and humidity
    def __init__(self):
        self.x = 0 
        self.y = 0 
        self.z = 0 
        self.o = 0
        self.sense = SenseHat()
        self.sense.clear()
       
        
    #read Accclerometer
    def readAccclerometer(self):
        self.o = self.sense.get_orientation()
        self.x = self.o["x"]
        self.y = self.o["y"]
        self.z = self.o["z"]
        print("x {0} y {1} z {2}".format(self.x,self.y,self.z))
        return self.x,self.y,self.z
    






