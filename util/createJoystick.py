#!/bin/env python
import pygame
import socket
import sys

PORTNUM = 6969
UPDATE = .0001
DEAD = .005

pygame.init()
pygame.joystick.init()
joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]

joystick = joysticks[0]
joystick.init()

mySocket = socket.socket ( socket.AF_INET, socket.SOCK_STREAM )

mySocket.connect( (sys.argv[1] , PORTNUM) )

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
	mySocket.send("cdd "+lpower+" "+rpower +"\n")

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

cooldown = 0

mySocket.send("ccn\n")
while True:
	pygame.event.pump()
	cooldown+=1
	if(cooldown > 100):
		horiz = joystick.get_axis(0)
		vert  = joystick.get_axis(1)

		if(lbutton != bool(joystick.get_button(3))):
			lbutton = joystick.get_button(3)
			handle_lbutton(lbutton)
		if(rbutton != bool(joystick.get_button(4))):
			rbutton = joystick.get_button(4)
			handle_rbutton(rbutton)
		if(joystick.get_button(2)):
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
		cooldown = 0

