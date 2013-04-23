import socket

PORTNUM = 7777

mySocket = socket.socket ( socket.AF_INET, socket.SOCK_STREAM )


print 'IP address to connect to? '

ipaddr = raw_input() 

mySocket.connect( ( ipaddr , PORTNUM) )
while True:
	thisLine = raw_input()
	mySocket.send(thisLine+"\n")
	
