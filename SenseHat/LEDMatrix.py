from sense_hat import SenseHat
class LEDMatrix(object): # Temp and humidity
    def __init__(self):
        self.x = 0
        self.y = 0  
        self.sense = SenseHat()
        self.sense.close()
        
    #read Tempreture
    def displayStr(self,str,x,y):
        #self.temp = sensehat.readTemp()
        self.sense.show_message(str, text_colour=[185, 139, 231])
        

        
