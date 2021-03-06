#!/usr/bin/env python
import sys
import socket
import time
import Commands_gen
from ctypes import cdll
from Commands_gen import *


#If set to true, then is verbose and uses alternate shared object library..
DEBUG = False


# Tells the server to return a line after each command is processed, allowing the
# client to know not to send more lines than can be processed at once
# (Not yet implemented in client-side code.)
RESPONSE = ""

# If you're recording to a C file, this is how it starts. If in competition
# uncomment the second line, otherwise just leave it
RECORDPREFIX = "int main() {\n"
#RECORDPREFIX = "int main() {\n wait_for_light(0); \n shut_down_in(110); \n"


# Port number, if you edit this make sure you edit it in client-side code as well.
PORT_NUM = 7777

#default value
outfile = False

# Handles the parsing  of a command line and returns the Command object representing
# the command sent to it.
def handleLine(thisLine, lib):
    thisLine = thisLine.split()
    thisPrefix = thisLine[0].lower()

    # Remove the string prefix from the command line
    thisLine.pop(0)

    # Parse integers out of the rest of the command line
    theseArgs = [int(i) for i in thisLine]

    # Just some echo output
    print thisPrefix + " " + str(theseArgs)
    return getCommand(thisPrefix, theseArgs,lib)

# Gets the command represented by a given prefix with the arguments from an int array
def getCommand(prefix, args, lib):
	# Uses the dictionary in the generated Commands_gen file to look up the
	# command class, then instantiates and populates a new instance
	if prefix in Commands_gen.commandSet:
		thisCommand = Commands_gen.commandSet[prefix]()
		thisCommand.create_from(args,lib)
		return thisCommand

	# If the prefix isn't found, simply return a command that does nothing and
	# represents no text
	return Command()


# If recording, then write an msleep equal to the time between commands, then the C commands
# that were executed
def writeCommand(command, ds):
	if(outfile):
		outFile.write("msleep("+str(ds)+");\n")
		outFile.write(command.toCommands())		

#checks for a certain string as the first element of the provided arguments,
#removes it if it's present and returns true otherwise returns false
def checkSpecial(checkFor):
    if(len(sys.argv) > 1 and sys.argv[1] == checkFor):
        sys.argv.pop(1)
        return True
    else:
        return False




def run_server():

    # This is the library that wraps Kovan API functions into a shared object library,
    # ctypes allows us to make calls to robot functions through python.
    # Another shared object library should be present wrapping debug functions.
    if(DEBUG):
        lib = cdll.LoadLibrary('./libDebug.so')
    else:
        lib = cdll.LoadLibrary('./libControl.so')

    print 'Accepting commands..'

    # Open a standard server socket
    thisSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    # This just lets us use the same port even if the last server didn't cleanly exit without a timeout
    thisSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)

    # Bind the server to the port
    thisSocket.bind( ('',PORT_NUM) )

    # Allow incoming connections
    thisSocket.listen(1)

    # Outfile opens if a command-line argument was passed to it
    outfile = ''
    if(len(sys.argv) > 1):
    	outfile = sys.argv[1]
    	print 'Network handler writing to: ', outfile
    	
    # If a recording is being made, open it and write the prefix
    if(outfile):
	outFile = open('/kovan/binaries/' + outfile.strip()+'.c','w')
	outfile.write(RECORDPREFIX)


    # Accept a connection over the socket
    channel, details = thisSocket.accept()

    # Make the channel into a file object to simplify read/writes
    channelFile = channel.makefile()

    print 'Connection recieved: ',details

    while True:
    #	Get the current time before processing the command
    	currentTime = time.time()

    #	Get the command sent over the connection
    	result = channelFile.readline()

    	print result

    #	If it's set to respond, send the response code
    	if(RESPONSE):
    		channelFile.write(RESPONSE+"\n")
    		channelFile.flush()

    	if(result.split()[0] == "END"):
    		break
    	command = handleLine(result,lib)
    	ds = 1000*(time.time() - currentTime)
    	writeCommand(command,ds)
    	command.execute()

    if( outfile ):
    	outFile.write('\nreturn 0;\n}')
    	outFile.flush()
    	outFile.close()
    thisSocket.close()
    lib.lib_ao()

if(__name__ =='__main__'):
    DEBUG = checkSpecial('debug')

    if(checkSpecial('repeat')):
        while(True):
            run_server()
    else:
        run_server()
