# 3V/5V HC SR04 ULTRASONIC SENSOR Python Program Example:

# Created by and taught by Paul McWhorter, toptechboy.com
# Learned by Joseph C. Richardson, GitHub.com

# Please note: I did not create this Python program
# example. However, I did discover that the variables
# and the values have to be in their correct order as
# shown in this Python program example below.

# Note: be mindful while working with
# electronics. There are mistakes that
# cannot be corrected should you ignore
# any basic electronics rules. Electronics
# demands basic math skills and knowledge
# of electronics components alike.

# Items needed are as follows:

# Raspberry Pi 4 = 1
# breadboard = 1
# 3V/5V HC SR04 Ultrasonic Sensor = 1
# jumper wire = 4, +2 for the Rasp pi 4 fan

# Note: use two other jumper wires for
# the Raspberry Pi 4 fan, while in use/
# operation.

# 3V/5V HC SR04 ULTRASONIC SENSOR Python Program Example:

# This Raspberry Pi 4 Python program allows
# users to have tons of fun, while learning
# how to use the HC SR04 Ultrasonic Sensor.

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
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Note: Python executes its programs from the top, downward.
# You must place these variable values in this correct order as shown.
# These pinout values won't execute right if you don't.

stop_program_message='''
print('Paul McWhorter: GPIO is good to go')
'''
trig,echo=13,11

GPIO.setup(trig,GPIO.OUT)
GPIO.setup(echo,GPIO.IN)

# Always use a KeyboardInterrupt, try and except error handler to force
# all GPIO pinouts to shut down to LOW/OFF state.

# Note: it is recommended that you setup a KeyboardInterrupt handler to force
# the GPIO pins to return to a low state/off via, pressing control+c

try:
    while True:
        GPIO.output(trig,0)
        time.sleep(2E-6)
        GPIO.output(trig,1)
        time.sleep(10E-6)
        GPIO.output(trig,0)
        while GPIO.input(echo)==0:
            pass
        echo_start=time.time()
        while GPIO.input(echo)==1:
            pass
        echo_stop=time.time()
        ping_travel=echo_stop-echo_start
        print(int(ping_travel*1E6))
        pause(.2)
                
except KeyboardInterrupt:
    GPIO.cleanup() # GPIO.cleanup() sets all GPIO pins to LOW/OFF state
    exec(stop_program_message)
