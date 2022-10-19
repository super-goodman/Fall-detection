import numpy as np
import smtplib
import time


#email variables
SMTP_SERVER='smtp.gmail.com'
SMTP_PORT=587
GMAIL_USERNAME='AUTFallDetection@gmail.com'
GMAIL_PASSWORD = 'jvnofyyztryoorzj'

producer=False
consumer=True

class Emailer:
    def sendmail(self, recipient, subject, content):

        #Create Headers
        headers = ["From: " + GMAIL_USERNAME, "Subject: " + subject, "To: "+recipient, "MIME-Version: 1.0", "Content-Type: text/html"]
        headers = "\r\n".join(headers)
        #Connect to Gmail Server
        session = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        session.ehlo()
        session.starttls()
        session.ehlo()

        #Login to Gmail
        session.login(GMAIL_USERNAME, GMAIL_PASSWORD)

        #Send Email & Exit
        session.sendmail(GMAIL_USERNAME, recipient, headers + "\r\n\r\n" + content)
        time.sleep(10)
        consumer=True
        session.quit

