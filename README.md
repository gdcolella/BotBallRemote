BotBallRemote
=============

Library for remote control of a KIPR Link and example client-side software.

INSTALLATION
------------

Go in to the build folder and run make, it will generate the upload folder with all the files that should be pushed to the robot.

Then, run remoteinstall.sh with the ipaddress of the robot, and it will be installed.


RUNNING

The usual way to run the server is over ssh. Execute 
>python /kovan/network/networkHandler.py
to begin running the server. 

Another way to run the server is through the ServerRunner program that is installed to /kovan/binaries ( and should be accessible
through the GUI onboard, if you're CLI averse).  





