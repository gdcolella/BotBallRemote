BotBallRemote
=============

Library for remote control of a KIPR Link and example client-side software.

This is licensed under the MIT license, feel free to do just about anything you wish with it.

If you find errors, have suggestions, or even find this somewhat useful, shoot me an email at Gregory.Colella@gmail.com .


##INSTALLATION
------------

###NOTE:
	This requires jinja2 and pygame to be installed.

Go in to the build folder and run make, it will generate the upload folder with all the files that should be pushed to the robot.

Then, run remoteinstall.sh with the IP address of the robot as an argument, and it will be installed.


##RUNNING
-------

The usual way to run the server is over ssh. Execute 

>python /kovan/network/networkHandler.py

to begin running the server. 

Another way to run the server is through the ServerRunner program that is installed to /kovan/binaries ( and should be accessible
through the GUI onboard, if you're CLI averse).  





