__author__ = 'madsens'
import Lights
import sys
sys.path.append("/home/pi/PiClasses")
import Logging
import time
import os

time.sleep(15)

dbConn = Logging.Logging()

dbConn.logBoot()

lastScan = 0
previousFile = ""
Lights.setup()
os.system("/home/pi/Halloween2015/Scripts/enableRFID.sh")

while True:    # Runs until break is encountered. We want to set it to break on a particular ID.
    n = raw_input("Scanned ID: ")
    currentScan = time.time()
    if n == "STOP":
        break  # stops the loop
    else :
        dbConn.logAccess(n)

        #Disable RFID
        os.system("/home/pi/Scripts/disableRFID.sh")

        #Trigger GPIO Pins. Trixie just uses pin 13
        Lights.on([13])

        time.sleep(1)

        #Play Creepy Laugh
        os.system('mpg321 /home/pi/Assets/TrixieBlinkChimes.mp3 -q')

        #Trixie GPIO Off
        Lights.off([13])

        #Log Activation of PI
        #Logging.LogAudioAccess(n, previousFile)

        #Reenable RFID
        os.system("/home/pi/Scripts/enableRFID.sh")