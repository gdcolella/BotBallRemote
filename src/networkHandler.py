#!/usr/bin/env python
import sys
import socket
import time
import Commands_gen
from ctypes import cdll
from Commands_gen import *

# This is the library that wraps Kovan API functions into a shared object library,
# ctypes allows us to make calls to robot functions through python.
lib = cdll.LoadLibrary('./libControl.so')


# Tells the server to return a line after each command is processed, allowing the
# client to know not to send more lines than can be processed at once
# (Not yet implemented in client-side code.)
SERVERANSWER = False

# Port number, if you edit this make sure you edit it in client-side code as well.
PORT_NUM = 7777



# Outfile opens if a command-line argument was passed to it 
outfile = ''
if(len(sys.argv) > 1):
	outfile = sys.argv[1]
	print 'Network handler writing to: ', outfile


# Handles the parsing  of a command line and returns the Command object representing
# the command sent to it.
def handleLine(thisLine):
	thisLine = thisLine.split()
        thisPrefix = thisLine[0].lower()

	# Remove the string prefix from the command line
        thisLine.pop(0)

	# Parse integers out of the rest of the command line
        theseArgs = [int(i) for i in thisLine]

	# Just some echo output
	print thisPrefix + " " + str(theseArgs)

	return getCommand(thisPrefix, theseArgs)

# Gets the command represented by a given prefix with the arguments from an int array
def getCommand(prefix, args):
	# Uses the dictionary in the generated Commands_gen file to look up the
	# command class, then instantiates and populates a new instance
	if thisPrefix in Commands_gen.commandSet:
		thisCommand = Commands_gen.commandSet[thisPrefix]()
		thisCommand.create_from(args)
		return thisCommand

	# If the prefix isn't found, simply return a command that does nothing and 
	# represents no text
	return Command()	


# Start of execution code
print 'Accepting commands..'

# Open a standard server socket
thisSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# This just lets us use the same port even if the last server didn't cleanly exit without a timeout
thisSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)

# Bind the server to the port
thisSocket.bind( ('',PORT_NUM) )

# Allow incoming connections
thisSocket.listen(1)

if(outfile):
	outFile = open('/kovan/binaries/' + outfile.strip()+'.c','w')
	outFile.write('int main() {\n wait_for_light(0); \n shut_down_in(110); \



def writeCommand(command, ds):
	if(outfile):
		outFile.write("msleep("+str(ds)+");\n")
		outFile.write(command.toCommands())
		

channel, details = thisSocket.accept()
channelFile = channel.makefile()
print 'Connection recieved: ',details
while True:
	currentTime = time.time()
	result = channelFile.readline()
	print result

	if(SERVERANSWER):
		channelFile.write("READ\n")
		channelFile.flush()

	if(result.split()[0] == "END"):
		break
	command = handleLine(result)
	ds = 1000*(time.time() - currentTime)
	writeCommand(command,ds)
	command.execute()

if( outfile ):
	outFile.write('\nreturn 0;\n}')
	outFile.flush()
	outFile.close()
thisSocket.close()
lib.lib_ao()
