# 16b LED Binary Template Functions Python
# program example:

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
# 74HC595 shift register = 2
# LEDs = 16
# 220 ohm resistor = 16
# jumper wire = 32 +2 for the Rasp Pi 4 fan

# Note: use two other jumper wires for
# the Raspberry Pi 4 fan, while in use/
# operation.

# 16b Led Binary Template Functions Python
# program example:

# This Raspberry Pi 4 Python program allows
# users to learn all about how binary data
# bits work with the 74HC595 shift register.
# Users can have some serious LED binary fun.

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

latch=33
data_bit=35
clock=31
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
msb=65535,65536 # most significant bits
lsb=32767,32768 # least significant bits

led_speed=.5 # pause duration

stop_program_message='''
print('Stop program Execution/run:')
print('cleanup/release all GPIO pinouts \
to LOW state.')'''

control_shift=data_bit,latch,clock

for i in control_shift:GPIO.setup(i,GPIO.OUT)

def clear_all_data_bits():
    
    for i in range(16):            
        GPIO.output(latch,0)
        GPIO.output(data_bit,0)
        GPIO.output(clock,1)
        GPIO.output(latch,1)
        GPIO.output(clock,0)

def binary_leds_default():
    
    for i in range(msb[0],lsb[0],-1):
        for j in range(16):
            bin=f'{i:b}'
            GPIO.output(latch,0)
            GPIO.output(data_bit,int(bin[j])-1)
            GPIO.output(clock,1)
            GPIO.output(latch,1)
            GPIO.output(clock,0)
        wait(led_speed)
    
    for i in range(lsb[1],msb[1]):
        for j in range(16):
            bin=f'{i:b}'
            GPIO.output(latch,0)
            GPIO.output(data_bit,int(bin[j]))
            GPIO.output(clock,1)
            GPIO.output(latch,1)
            GPIO.output(clock,0)
        wait(led_speed)
        
def binary_leds_inverse():
    
    for i in range(msb[0],lsb[0],-1):
        for j in range(16):
            bin=f'{i:b}'
            GPIO.output(latch,0)
            GPIO.output(data_bit,int(bin[j]))
            GPIO.output(clock,1)
            GPIO.output(latch,1)
            GPIO.output(clock,0)
        wait(led_speed)
    
    for i in range(lsb[1],msb[1]):
        for j in range(16):
            bin=f'{i:b}'
            GPIO.output(latch,0)
            GPIO.output(data_bit,int(bin[j])-1)
            GPIO.output(clock,1)
            GPIO.output(latch,1)
            GPIO.output(clock,0)
        wait(led_speed)

def binary_leds_mirror():
    
    for i in range(msb[0],lsb[0],-1):
        for j in range(7,-1,-1):
            bin=f'{i:b}'
            GPIO.output(latch,0)
            GPIO.output(data_bit,int(bin[j])-1)
            GPIO.output(clock,1)
            GPIO.output(latch,1)
            GPIO.output(clock,0)
        wait(led_speed)
    
    for i in range(lsb[1],msb[1]):
        for j in range(7,-1,-1):
            bin=f'{i:b}'
            GPIO.output(latch,0)
            GPIO.output(data_bit,int(bin[j]))
            GPIO.output(clock,1)
            GPIO.output(latch,1)
            GPIO.output(clock,0)
        wait(led_speed)
        
def binary_leds_mirror_inverse():
    
    for i in range(msb[0],lsb[0],-1):
        for j in range(7,-1,-1):
            bin=f'{i:b}'
            GPIO.output(latch,0)
            GPIO.output(data_bit,int(bin[j]))
            GPIO.output(clock,1)
            GPIO.output(latch,1)
            GPIO.output(clock,0)
        wait(led_speed)
    
    for i in range(lsb[1],msb[1]):
        for j in range(7,-1,-1):
            bin=f'{i:b}'
            GPIO.output(latch,0)
            GPIO.output(data_bit,int(bin[j])-1)
            GPIO.output(clock,1)
            GPIO.output(latch,1)
            GPIO.output(clock,0)
        wait(led_speed)
        
clear_all_data_bits()

led_binary_functions_demo=(
    binary_leds_default,
    binary_leds_inverse,
    binary_leds_mirror,
    binary_leds_mirror_inverse)
    
while True:
    try:
        for i in led_binary_functions_demo:i()
        clear_all_data_bits()
        break
    
# Note: it is recommended that you setup
# a KeyboardInterrupt handler to force
# the GPIO pins to return to a low state/off.

# GPIO.cleanup() sets all GPIO pins to LOW/OFF

    except KeyboardInterrupt:
        exec(stop_program_message) # GPIO notification message
        
        clear_all_data_bits()            
        GPIO.cleanup() # GPIO.cleanup() sets all GPIO pins to LOW/OFF
        break
