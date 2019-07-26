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
SLEEPTIME = .1

# GPIO PINS FOR LED AND BUTTON
LED_GPIO_PIN = 7
BTN_GPIO_PIN = 11

# Setting up the mode of the numbering system
GPIO.setmode(GPIO.BOARD)

# Setting up the output pin to use the LED & setting the LED default value to false
GPIO.setup(LED_GPIO_PIN, GPIO.OUT)
GPIO.output(LED_GPIO_PIN, False)

# Setting up the input pin the BUTTON &
# Using the Broadcom chip's pull-up resistor - so that we don't physically configure it in our breadboard
# Specifially using the pull-up resistor not the pull-down
GPIO.setup(BTN_GPIO_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Logic that you write
def main():
    print("About to run the code")

    # Taking the output and setting it using the input value from the button at any point in time
    GPIO.output(LED_GPIO_PIN, GPIO.input(BTN_GPIO_PIN))
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
        GPIO.output(LED_GPIO_PIN, False)

        # CLEARING WHAT THE PINS HAVE BEEN PROGRAMMED
        GPIO.cleanup()
    except  :
        GPIO.cleanup()
        print("Some other error occurred")
        print(e.message)