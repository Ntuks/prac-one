#!/usr/bin/python3
"""
Names: NTUTHUKO MPAKU
Student Number: MPKNTU001
Prac: 1
Date: 7/23/2019
Description: Testing how to switch an LED on with a button that is configured by the Raspberry PI
"""

# import Relevant Librares
import RPi.GPIO as GPIO
from time import sleep
import itertools as iter

# Sleep time for the buttons to wait long enough
SLEEPTIME = 2

# GPIO PINS FOR LED AND BUTTON
LEDS = [7, 11, 13]
BTNS = [16,18]

def init():
    print("Initializing...")
    # Setting up the mode of the numbering system
    GPIO.setmode(GPIO.BOARD)

    # Setting up the output pin to use the LED & setting the LED default value to false
    for LED in LEDS:
        GPIO.setup(LED, GPIO.OUT)
        GPIO.output(LED, False)

    # Setting up the input pin the BUTTON & Using the Broadcom chip's pull-up resistor -
    # so that we don't physically configure iter in our breadboard - these are for debouncing
    GPIO.setup(BTNS[0], GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(BTNS[1], GPIO.IN, pull_up_down=GPIO.PUD_UP)

    GPIO.add_event_detect(BTNS[0], GPIO.RISING, callback=binaryIncrement, bouncetime=200)  # add rising edge detection on a BTNS
    GPIO.add_event_detect(BTNS[1], GPIO.RISING, callback=binaryDecrement, bouncetime=200)  # add rising edge detection on a BTNS


# Logic that you write
def main():
    print("Waiting For Button to be pressed")

""" THIS FUNCTION LIGHTS UP THE LEDS IN A BINARY COUNTING INCREMENTING FASHION """
def binaryIncrement(channel):
    print("Binary Increment")
    # This code is for making sure that the counter wraps around.
    global index 
    if index == len(values)-1:
        index = 0
    else:
        index+1    

    ON = list(iter.compress(LEDs, values[index]))   
    OFF = [LED for LED in LEDs if LED not in ON]    
    GPIO.output(ON, GPIO.HIGH)
    GPIO.output(OFF, GPIO.LOW)

""" THIS FUNCTION LIGHTS UP THE LEDS IN A BINARY COUNTING DECREMENTING FASHION """
def binaryDecrement(channel):
    # This code is for making sure that the counter wraps around.
    print("Binary Decrement")
    global index
    if index == 0:
        index = len(values)-1  
    else:
        index-1    

    ON = list(iter.compress(LEDs, values[index]))
    OFF = [LED for LED in LEDs if LED not in ON]
    GPIO.output(ON, GPIO.HIGH)
    GPIO.output(OFF, GPIO.LOW)
    


# Only run the functions if
if __name__ == "__main__":
    # Make sure the GPIO is stopped correctly
    try:
        init()
        while True:
            main()
    except KeyboardInterrupt:
        print("Exiting gracefully")
        # Turn off your GPIOs here
        for LED in LEDS:
            GPIO.output(LED, False)

        # CLEARING WHAT THE PINS HAVE BEEN PROGRAMMED
        GPIO.cleanup()
    except:
        GPIO.cleanup()
        print("Some other error occurred")
