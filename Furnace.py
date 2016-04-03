__author__ = 'madsens'
import sys
sys.path.append("/home/pi/Python/PiClasses")
import os
import Movies
import time

# This code runs the Furnace

print 'Starting'
Movies.StartLoop('/home/pi/Assets/Furnace')

while True:    # Runs until break is encountered. We want to set it to break on a particular ID.
    #Logging.HeartBeat()
    n = raw_input("Scanned ID: ")
    if n == "STOP":
        Movies.StopLoop()
        print "Stopping."
        break  # stops the loop
    else :
        # On Input, Disable Reader
        os.system("/home/pi/NYE2015/Scripts/disableRFID.sh")
        print "Playing."
        Movies.PlayMovie()

        time.sleep(18)
        # Reenable reader.
        os.system("/home/pi/NYE2015/Scripts/enableRFID.sh")