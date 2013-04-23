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

#mySocket = socket.socket ( socket.AF_INET, socket.SOCK_STREAM )

#mySocket.connect( (sys.argv[1] , PORTNUM) )

power = 100
clawpower = 20

def handle_lbutton(cmd):
	if(cmd):
		print ("mtr 0 "+str(-1*clawpower)+"\n")
	else:
		print("mtr 0 0\n")

def handle_rbutton(cmd):
	if(cmd):
		print("mtr 0 "+str(clawpower)+"\n")
	else:
		print("mtr 0 0\n")

def handle_mbutton(cmd):
	print ""

def handle_axes(vert, horiz):
	lpower = str(int(vert*power) - int(horiz*power) )
	rpower = str(int(vert*power) + int(horiz*power) )
	print ("mmr 1 "+lpower+" 3 "+rpower +"\n")

def handle_horiz(axis):
	pwr = str(int(axis*power))
	npwr = str(int(axis*power*-1))
	print ("mmr 1 "+pwr+" 3 "+npwr+"\n")


def handle_vert(axis):
	pwr = str(int(axis*power))
	print ("mmr 1 "+pwr+" 3 "+pwr+"\n")

lasthoriz = 0
lastvert  = 0
dead = False

lbutton = False
rbutton = False
mbutton = False

while True:
	pygame.event.pump()
	horiz = joystick.get_axis(0)
	vert  = joystick.get_axis(1)

	if(joystick.get_button(2)):
		print "~~~~~~~~~~~~"

	if(lbutton != bool(joystick.get_button(3)) ):
		lbutton = bool(joystick.get_button(3))
		handle_lbutton(lbutton)
	if(rbutton != bool(joystick.get_button(4)) ):
		rbutton = bool(joystick.get_button(4 ))
		handle_rbutton(rbutton)
		

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

