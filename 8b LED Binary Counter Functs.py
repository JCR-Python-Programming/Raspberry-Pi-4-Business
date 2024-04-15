# 8b LED Binary Counter Functions Python program example:

# Created by Joseph C. Richardson, GitHub.com

# Note: be mindful while working with
# electronics. There are mistakes that
# cannot be corrected should you ignore
# any basic electronics rules. Electronics
# demands basic math skills and knowledge
# of electronics components alike.

# Items needed are as follows:

# Raspberry Pi 4 = 1
# breadboard = 1 or more depending
# 74HC595 shift register = 1
# LEDs = 8
# 220 ohm resistor = 8
# jumper wire = 15 +2 for the Rasp pi 4 fan

# Note: use two other jumper wires for
# the Raspberry Pi 4 fan, while in use/
# operation.

# 8b Binary Counter Python program example:

# This Raspberry Pi 4 Python program allows
# users to learn all about how binary data
# bits work with the 74HC595 shift register.

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

import RPi.GPIO as GPIO
from time import sleep as wait

GPIO.setmode(GPIO.BOARD) # breadboard method
GPIO.setwarnings(False) # disable setwarnings

# Create variables for the latch, data bit and the clock.

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
# You must place these variables in this correct order as shown.
# These pinout values won't execute right if you don't.

latch=35
data_bit=37
clock=33
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
msb=255,256 # most significant bits
lsb=127,128 # least significant bits

led_speed=.5 # pause duration

stop_program_message='''
print('Stop program Execution/run:')
print('cleanup/release all GPIO pinouts \
to LOW state.')'''

control_shift=latch,data_bit,clock

for i in control_shift:GPIO.setup(i,GPIO.OUT) # setup desired GPIO pinouts

# Create two functions called:

# clear_all_data_bits
# shift_all_data_bits

def clear_all_data_bits():

    for i in range(8):
        GPIO.output(latch,0)
        GPIO.output(data_bit,0) # set all 8 data bits to 0/off
        GPIO.output(clock,1)
        GPIO.output(latch,1)
        GPIO.output(clock,0)
        
def shift_all_data_bits():

    for i in range(msb[0],lsb[0],-1): # reverse for loop and step value -1
        bin=f'{i:b}'
        for j in range(8):
            GPIO.output(latch,0)
            GPIO.output(data_bit,int(bin[j])-1) # with 2's complement value -1
            GPIO.output(clock,1)
            GPIO.output(latch,1)
            GPIO.output(clock,0)
        wait(led_speed)

    for i in range(lsb[1],msb[1]): # forward for loop
        bin=f'{i:b}'
        for j in range(8):
            GPIO.output(latch,0)
            GPIO.output(data_bit,int(bin[j])) # without 2's complement
            GPIO.output(clock,1)
            GPIO.output(latch,1)
            GPIO.output(clock,0)
        wait(led_speed)

clear_all_data_bits()

try:
    shift_all_data_bits()

# Note: it is recommended that you setup
# a KeyboardInterrupt handler to force
# the GPIO pins to return to a low state/off.

except KeyboardInterrupt:
    exec(stop_program_message) # GPIO notification message

    clear_all_data_bits() # call the function
    
GPIO.cleanup() # GPIO.cleanup() sets all GPIO pins to LOW/OFF
