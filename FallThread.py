import threading
from SenseHat.ICM20948 import ICM20948
from time import sleep
import io
import time
import os
import sys, getopt
import signal
import time
from Email import Emailer
from sqlite3 import Cursor
import pymysql
from edge_impulse_linux.runner import ImpulseRunner


#change email address for recipient here"
sendTo = 'denismizhou@gmail.com'
#change email address for recipient here"

emailSubject = "User Fall detected! Check with them to see if they are fine"
emailContent = "This Fall detection device has detected a fall from the user, you may want to check up with him/her to see if they are Okay./nThis is an auto generated E-mail."

runner = None

def signal_handler(sig, frame):
    print('Interrupted')
    if (runner):
        runner.stop()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

def help():
    print('python classify.py <path_to_model.eim> <path_to_features.txt>')


def classify():

    model = "modelfile.eim"
    features_file = io.open("data.txt", 'r', encoding='utf8')
    features = features_file.read().strip().replace('\n','').split(',')

    if '0x' in features[0]:
        features = [float(int(f, 16)) for f in features]
    else:
        features = [float(f) for f in features]


    dir_path = os.path.dirname(os.path.realpath(__file__))
    modelfile = os.path.join(dir_path, model)

    print('MODEL: ' + modelfile)


    runner = ImpulseRunner(modelfile)
    try:
        model_info = runner.init()
        print('Loaded runner for "' + model_info['project']['owner'] + ' / ' + model_info['project']['name'] + '"')
        
        res = runner.classify(features)
        print("classification:")
        print(res["result"])
        print("timing:")
        print(res["timing"])
        return res["result"]
    finally:
        if (runner):
            runner.stop()


class FallThread (threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.acc = ICM20948()
        self.sender=Emailer()
        # Please use your own server
        self.db = pymysql.connect(host='117.50.162.94',user='***',password='***',database='bot')
        self.cursor = self.db.cursor()
    def run(self):
        while 1:
            contG = 9.80665
            arr = []
            self.start = time.time()
            for i in range (800):
                x,y,z = self.acc.readAccclerometer()
                ax = ((2*16) / (2**13)) * x * contG
                ay = ((2*16) / (2**13)) * y * contG
                az = ((2*16) / (2**13)) * z * contG
                arr.append([ax, ay, az]) 
            print(time.time()-self.start)
            f = open("data.txt","w")
            for j in range (800):
                toWrite = str(arr[j])
                toWrite = toWrite.replace('[','')
                toWrite = toWrite.replace(']','')
                f.write(toWrite)
                if j < 800:  
                    f.write(',\n')
            f.close()
            print ("writing finished!")
            #classify 
            result = classify()
            #Send mail if the result is fall
            if result == 1:
                self.sender.sendmail(sendTo, emailSubject, emailContent)  
                sql = "INSERT INTO `Record` (`Content`,`Time`) VALUES (\"Fall\",{0})".format(time.time())
                self.cursor.execute(sql)
                result = self.cursor.fetchall()
                print(result)
     
        
        
