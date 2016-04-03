__author__ = 'madsens'
import sys
sys.path.append("/home/pi/Python/PiClasses")
import os
import Movies
import time
import Lights

# This code runs the Furnace
Lights.setup()

print 'Starting'
#Movies.StartLoop('/home/pi/Assets/Furnace')

while True:    # Runs until break is encountered. We want to set it to break on a particular ID.
    #Logging.HeartBeat()
    n = raw_input("Scanned ID: ")
    Lights.showColor("gold")
    if n == "STOP":
        #Movies.StopLoop()
        Lights.cleanup()
        print "Stopping."
        break  # stops the loop
    else :
        # On Input, Disable Reader
        #os.system("/home/pi/NYE2015/Scripts/disableRFID.sh")
        print "red"
        Lights.showColor("red")
        time.sleep(2)
        print "none"
        Lights.showColor("none")
        print "Playing."
        #Movies.PlayMovie()

        time.sleep(5)
	Lights.showColor("gold")
        # Reenable reader.
        #os.system("/home/pi/NYE2015/Scripts/enableRFID.sh")
