#!/usr/bin/env python

import serial
usbCom = serial.Serial('/dev/ttyUSB0', 9600)


from evdev import InputDevice, categorize, ecodes, KeyEvent
from evdev.ecodes import keys, KEY, ABS, EV_ABS
gamepad = InputDevice('/dev/input/event6')


for event in gamepad.read_loop():
    if event.type == ecodes.EV_ABS:
	abs_event = categorize(event)
	#valeur (1 ou 0 ou -1)
	value = abs_event.event.value
	#(16 = horizontal, 17 vertical)
	code = abs_event.event.code

	
	if(code == 16 and value == 1):
	    print("tourne a droite")
	    command = 'D'
	elif(code == 16 and value == -1):
	    print("tourne a gauche")
	    command = 'G'
	elif(code == 17 and value == 1):
	    print("recul")
	    command = 'R'
	elif(code == 17 and value == -1):
	    print("avance caliss")
	    command = 'A'
	elif(value == 0):
	    print("arrete toute")
	    command = '0'
	usbCom.write(command)


