#!/usr/bin/env python3
import RPi.GPIO as GPIO # Import the GPIO Library
import time             # Import the Time library


# Set the GPIO modes
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Set variables for the GPIO pins
pinLineFollower = 25

# Set pin 25 as an input so its value can be read
GPIO.setup(pinLineFollower, GPIO.IN)

try:
 # Repeat the next indented block forever
   while True:
    # If the sensor is High it’s above the white line
    if GPIO.input(pinLineFollower)==0:
     print("The sensor is seeing a white surface")
     # If not... 
    else:
     print("The sensor is seeing a black surface")
     # Wait, then do the same again
     time.sleep(0.2)
     # If you press CTRL+C, cleanup and stop

except KeyboardInterrupt:
 GPIO.cleanup()
