# PASSIVE INFRARED SENSOR Python Program Example:

# Created by Joseph C. Richardson, GitHub.com

# Note: be mindful while working with
# electronics. There are mistakes that
# cannot be corrected should you ignore
# any basic electronics rules. Electronics
# demands basic math skills and knowledge
# of electronics components alike.

# Items needed are as follows:

# Raspberry Pi 4 = 1
# breadboard = 1
# PIR sensor = 1
# 5V active buzzer = 1
# LED = 1
# 220 ohm resistor = 1
# jumper wire = 7, +2 for the Rasp pi 4 fan

# Note: use two other jumper wires for
# the Raspberry Pi 4 fan, while in use/
# operation.

# PASSIVE INFRARED SENSOR Python Program Example:

# This Raspberry Pi 4 Python program allows
# users to have tons of fun, while learning
# how to use the PIR (Passive Infrared Sensor)

# We will use the breadboard method:

# GPIO.setmode(GPIO.BOARD)

# This method is for the GPIO pinouts
# not the GPIO numbers, such as BCM

# You can also use the Broadcom SOC
# Channel method if you prefer:

# GPIO.setmode(GPIO.BCM)
# This allows GPIO numbers, not GPIO
# pinouts, such as the breadboard
# method illustrates in our Python
# program example.

# import functions:

import time,RPi.GPIO as GPIO
from time import sleep as pause
GPIO.setmode(GPIO.BOARD) # breadboard method
GPIO.setwarnings(False) # disable setwarnings

# You can rename all these variables to any names you wish,
# but keep in mind that you must also rename any variables
# in your program as well. Click the Find and Replace command
# on the IDLE menu to make any renaming changes faster to cover
# any variables you want to rename. However, you should stick
# to meaningful names, so other programmers can learn and
# understand what's happening throughout the program's
# execution/run.

stop_program_message='''
print('Stop program Execution/run:')
print('cleanup/release all GPIO pinouts \
to LOW state.')
'''
pin=11,13,15

GPIO.setup(pin[0],GPIO.IN)
GPIO.setup(pin[1],GPIO.OUT)
GPIO.setup(pin[2],GPIO.OUT)

# Always use a KeyboardInterrupt, try and except error handler to force
# all GPIO pinouts to shut down to LOW/OFF state.

# Note: it is recommended that you setup a KeyboardInterrupt handler to force
# the GPIO pins to return to a low state/off via, pressing control+c

try:
    while True:
        sensor=GPIO.input(pin[0])
        GPIO.output(pin[1],sensor)
        GPIO.output(pin[2],sensor)
        print('Sensor =',sensor)
        pause(.2)
        
except KeyboardInterrupt:
    GPIO.cleanup() # GPIO.cleanup() sets all GPIO pins to LOW/OFF state
    exec(stop_program_message)
