#!/usr/bin/python3
"""
Names: NTUTHUKO MPAKU
Student Number: MPKNTU001
Prac: 1
Date: 7/23/2019
Description: Testing how to switch an LED on with a Raspberry PI
"""

# import Relevant Librares
import time
import RPi.GPIO as GPIO

# Logic that you write
def main():
    print("About to run the code")
    # Setting up the mode of the numbering system
    GPIO.setmode(GPIO.BOARD)

    # Setting up the output pin to use & letting power through
    GPIO.setup(7, GPIO.OUT)
    GPIO.output(7, True) # can also use GPIO.HIGH & GPIO.LOW

    # Creating the blinking effect by stalling for a second & cutting the power
    time.sleep(5)
    GPIO.output(7, False)
    time.sleep(5)
    print("code has ran")


# Only run the functions if 
if __name__ == "__main__":
    # Make sure the GPIO is stopped correctly
    try:
        while True:
            main()
    except KeyboardInterrupt:
        print("Exiting gracefully")
        # Turn off your GPIOs here
        GPIO.cleanup()
    except e:
        GPIO.cleanup()
        print("Some other error occurred")
        print(e.message)