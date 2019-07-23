#!/usr/bin/python3
"""
Names: NTUTHUKO MPAKU
Student Number: MPKNTU001
Prac: 1
Date: 7/23/2019
Description: Testing the PI'S INPUTS AND OUTPUTS
"""

# import Relevant Librares
import time
import RPi.GPIO as GPIO

# Setting up the mode of the numbering system
GPIO.setmode(GPIO.BOARD)

# Setting up the output pin to use & letting power through
GPIO.setup(6, GPIO.OUT)
GPIO.output(6, True) # can also use GPIO.HIGH & GPIO.LOW

# Creating the blinking effect by stalling for a second & cutting the power
time.sleep(1)
GPIO.output(6, False)
