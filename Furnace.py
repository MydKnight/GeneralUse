__author__ = 'madsens'
import sys
sys.path.append("/home/pi/PiClasses")
import Logging
import os
import Movies
import time

dbConn = Logging.Logging()

dbConn.logBoot()

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
        dbConn.logAccess(n)

        # On Input, Disable Reader
        os.system("/home/pi/Scripts/disableRFID.sh")
        print "Playing."
        Movies.PlayMovie()
        time.sleep(18)
        # Reenable reader.
        os.system("/home/pi/Scripts/enableRFID.sh")
        Movies.PlayLoop()