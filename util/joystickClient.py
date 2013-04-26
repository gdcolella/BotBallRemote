#!/bin/env python
import pygame
import socket
import sys

PORTNUM = 7777
UPDATE = .0001
DEAD = .005

if(len(sys.argv) < 2):
	print "IP Address to connect to? "
	ipaddr = raw_input()
else:
	ipaddr = sys.argv[1]


pygame.init()
pygame.joystick.init()
joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]

if(len(joysticks)<1):
	print "Cannot connect to joystick.. is it connected? "
	sys.exit()

joystick = joysticks[0]
joystick.init()

mySocket = socket.socket ( socket.AF_INET, socket.SOCK_STREAM )

mySocket.connect( (ipaddr , PORTNUM) )

power = 100
clawpower = 20

def handle_lbutton(cmd):
	if(cmd):
		mySocket.send("mtr 0 "+str(-1*clawpower)+"\n")
	else:
		mySocket.send("mtr 0 0\n")

def handle_rbutton(cmd):
	if(cmd):
		mySocket.send("mtr 0 "+str(clawpower)+"\n")
	else:
		mySocket.send("mtr 0 0\n")

def handle_mbutton(cmd):
	print ""

def handle_axes(vert, horiz):
	lpower = str(int(vert*power) + int(horiz*power) )
	rpower = str(int(vert*power) - int(horiz*power) )
	mySocket.send("mmr 1 "+lpower+" 3 "+rpower +"\n")

def handle_horiz(axis):
	pwr = str(int(axis*power))
	npwr = str(int(axis*power*-1))
	mySocket.send("mmr 1 "+pwr+" 3 "+npwr+"\n")


def handle_vert(axis):
	pwr = str(int(axis*power))
	mySocket.send("mmr 1 "+pwr+" 3 "+pwr+"\n")

lasthoriz = 0
lastvert  = 0
dead = False

lbutton = False
rbutton = False
mbutton = False


def getAxis(axis):
	sys.stdout = os.devnull
	out = joystick.get_axis(axis)
	sys.stdout = sys.__stdout__
	return out

def getButton(button):
	sys.stdout = os.devnull
	out = joystic.get_button(button)
	sys.stdout = sys.__stdout__

while True:
	pygame.event.pump()
	
	sys.stdout = os.devnull
	horiz = getAxis(0)
	vert  = getAxis(1)

	if(lbutton != bool(getButton(3))):
		lbutton = getButton(3)
		handle_lbutton(lbutton)
	if(rbutton != bool(getButton(4))):
		rbutton = getButton(4)
		handle_rbutton(rbutton)
	if(joystick.getButton(2)):
		mySocket.send("END\n")
		break

	#print str(lasthoriz) + " is moving to " + str(horiz)
	if(not(dead) and abs(horiz) < DEAD and abs(vert) < DEAD):
		handle_horiz(0)
		dead = True
	else:
		if(abs(horiz-lasthoriz) > UPDATE or abs(vert-lastvert) > UPDATE):
			handle_axes(-vert,-horiz)
			dead = False
		
		lasthoriz = horiz
		lastvert = vert

