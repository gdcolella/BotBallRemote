#!/usr/bin/env python
import sys
import socket
import time
import Commands_gen
from ctypes import cdll
from Commands_gen import *

lib = cdll.LoadLibrary('./libControl.so')

PORT_NUM = 6969
writebuffer = ""

outfile = ''
if(len(sys.argv) > 1):
	outfile = sys.argv[1]
	print 'Network handler writing to: ', outfile


def handleLine(thisLine):
	thisLine = thisLine.split()
        thisPrefix = thisLine[0].lower()
        thisLine.pop(0)
        theseArgs = [int(i) for i in thisLine]

	print thisPrefix + " " + str(theseArgs)

	if thisPrefix in Commands_gen.commandSet:
		thisCommand = Commands_gen.commandSet[thisPrefix]()
		thisCommand.create_from(theseArgs)
		return thisCommand


	return Command()

print 'Accepting commands..'

thisSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
thisSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
thisSocket.bind( ('',PORT_NUM) )
thisSocket.listen(1)

if(outfile):
	outFile = open('/kovan/binaries/' + outfile.strip()+'.c','w')
	outFile.write('int main() {\n wait_for_light(0); \n shut_down_in(110); \n')
#	writebuffer += ('int main() {\n')



def writeCommand(command, ds):
	if(outfile):
		outFile.write("msleep("+str(ds)+");\n")
		outFile.write(command.toCommands())
		#outFile.flush()
	#	global writebuffer
	#	writebuffer.append("msleep("+str(ds)+");\n")
	#	writebuffer+=command.toCommands()


channel, details = thisSocket.accept()
channelFile = channel.makefile()
print 'Connection recieved: ',details
while True:
	currentTime = time.time()
	result = channelFile.readline()
	print result
	if(result.split()[0] == "END"):
		break
	command = handleLine(result)
	ds = 1000*(time.time() - currentTime)
	writeCommand(command,ds)
	command.execute()

if( outfile ):
#	outFile.write(writebuffer)
	outFile.write('\nreturn 0;\n}')
	outFile.flush()
	outFile.close()
thisSocket.close()
lib.lib_ao()
