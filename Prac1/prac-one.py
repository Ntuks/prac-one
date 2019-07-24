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

# VARIABLES TO MAKE THE CODE CLEANER?
SLEEPTIME = 1

# GPIO PINS FOR LED AND BUTTON
LEDS = [7, 11, 13]
BTNS = [16,18]
# LED1 = 7
# LED2 = 11
# LED3 = 13
# BTN1 = 16
# BTN2 = 18

def init():
    # Setting up the mode of the numbering system
    GPIO.setmode(GPIO.BOARD)

    # Setting up the output pin to use the LED & setting the LED default value to false
    for LED in LEDS:
        GPIO.setup(LED, GPIO.OUT)
        GPIO.output(LED, False)

    # GPIO.setup(LED, GPIO.OUT)
    # GPIO.output(LED, False)
    # GPIO.setup(LED, GPIO.OUT)
    # GPIO.output(LED, False)

    # Setting up the input pin the BUTTON &
    # Using the Broadcom chip's pull-up resistor - so that we don't physically configure it in our breadboard
    # Specifially using the pull-up resistor not the pull-down
    GPIO.setup(BTNS[0], GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(BTNS[1], GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Logic that you write
def main():
    print("About to run the code")
    init()
    GPIO.add_event_detect(BTNS[0], GPIO.RISING)  # add rising edge detection on a BTNS
    GPIO.add_event_detect(BTNS[1], GPIO.RISING)  # add rising edge detection on a BTNS
    if GPIO.event_detected(BTNS[1]):
        binaryIncrement()
    elif GPIO.event_detected(BTNS[1]):
        binaryDecrement()

""" THIS FUNCTION LIGHTS UP THE LEDS IN A BINARY COUNTING INCREMENTING FASHION """
def binaryIncrement()
    GPIO.output(LEDS[0], GPIO.input(BTNS[0]))
    sleep(SLEEPTIME)
    GPIO.output(LEDS[0], False)
    GPIO.output(LEDS[1], GPIO.input(BTNS[0]))
    sleep(SLEEPTIME)
    GPIO.output(LEDS[0], GPIO.input(BTNS[0]))
    sleep(SLEEPTIME)
    GPIO.output(LEDS[0], False)
    GPIO.output(LEDS[1], False)
    GPIO.output(LEDS[2], GPIO.input(BTNS[0]))
    sleep(SLEEPTIME)
    GPIO.output(LEDS[0], GPIO.input(BTNS[0]))
    sleep(SLEEPTIME)
    sleep(SLEEPTIME)
    GPIO.output(LEDS[1], GPIO.input(BTNS[0]))

""" THIS FUNCTION LIGHTS UP THE LEDS IN A BINARY COUNTING DECREMENTING FASHION """
def binaryDecrement()
    # Starting off with all the LEDs ON == 111
    for LED in LEDS:
        GPIO.output(LED, GPIO.input(BTNS[1]))
    sleep(SLEEPTIME)

    # Switching off LED2 == 110
    GPIO.output(LEDS[2], False)
    sleep(SLEEPTIME)

    # Switching off LED1 & Switching on LED2 back == 101
    GPIO.output(LEDS[1], False)
    GPIO.output(LEDS[2], GPIO.input(BTNS[1]))
    sleep(SLEEPTIME)

    # Switching off LED2 again == 100
    GPIO.output(LEDS[2], False)
    sleep(SLEEPTIME)

    # Switching on LED1 & LED2 again & Switching off LED0 == 011
    GPIO.output(LEDS[1], GPIO.input(BTNS[1]))
    GPIO.output(LEDS[2], GPIO.input(BTNS[1]))
    GPIO.output(LEDS[0], False)
    sleep(SLEEPTIME)

    # Switching off LED2 agaain == 010
    GPIO.output(LEDS[0], GPIO.input(BTNS[1]))
    sleep(SLEEPTIME)

    # Switching off LED1 & Switching on LED2 back == 001
    GPIO.output(LEDS[1], GPIO.input(BTNS[1]))
    sleep(SLEEPTIME)

# Only run the functions if 
if __name__ == "__main__":
    # Make sure the GPIO is stopped correctly
    try:
        while True:
            main()
    except KeyboardInterrupt:
        print("Exiting gracefully")
        # Turn off your GPIOs here
        for LED in LEDS:
            GPIO.output(LED, False)

        # CLEARING WHAT THE PINS HAVE BEEN PROGRAMMED
        GPIO.cleanup()
    except e:
        GPIO.cleanup()
        print("Some other error occurred")
        print(e.message)