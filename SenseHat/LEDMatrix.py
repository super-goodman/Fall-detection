from sense_hat import SenseHat
class LEDMatrix(object): 
    def __init__(self):

        self.sense = SenseHat()
        self.sense.clear()
        
  
    def displayStr(self,str,x,y):
        self.sense = SenseHat()
        self.sense.show_message(str, text_colour=[185, 139, 231])
        self.sense.clear()

        
