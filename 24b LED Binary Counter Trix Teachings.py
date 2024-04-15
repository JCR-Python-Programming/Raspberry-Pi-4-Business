# 24b LED Binary Counter Trix Teachings Python program example:

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
# 74HC595 shift register = 3
# 5V active buzzer = 2
# bar graph LED = 1
# LEDs = 14
# 220 ohm resistor = 24
# jumper wire = 36 or more +2 for the Rasp pi 4 fan

# Note: use two other jumper wires for
# the Raspberry Pi 4 fan, while in use/
# operation.

# 24b LED Binary Counter Trix Python program example:

# This Raspberry Pi 4 Python program allows
# users to have tons of fun, while learning
# how three 8b 74HC595 shift registers work.

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

import RPi.GPIO as GPIO,random
from time import sleep as wait

GPIO.setmode(GPIO.BOARD) # breadboard method
GPIO.setwarnings(False) # disable setwarnings

pin=11,13 # two Rasp Pi 4 pin values for buzzers

GPIO.setup(pin[0],GPIO.OUT) # buzzer 1
GPIO.setup(pin[1],GPIO.OUT) # buzzer 2

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
msb=16_777_215,16_777_216 # most significant bits
lsb=8_388_607,8_388_608 # least significant bits

led_speed=1,.05,.5 # pause duration

beep_on='''
GPIO.output(pin[0],1)
GPIO.output(pin[1],1)
'''
beep_off='''
GPIO.output(pin[0],0)
GPIO.output(pin[1],0)
'''
stop_program_message='''
print('Stop program Execution/run:')
print('cleanup/release all GPIO pinouts \
to LOW state.')
'''
control_shift=data_bit,latch,clock

for i in control_shift:GPIO.setup(i,GPIO.OUT) # setup desired GPIO pinouts

for i in range(24):            
    GPIO.output(latch,0)
    GPIO.output(data_bit,0)
    GPIO.output(clock,1)
    GPIO.output(latch,1)
    GPIO.output(clock,0)
    
def binary_bits_default():
    
    try:    
        for i in range(msb[0],lsb[0],-1):
            bin=f'{i:b}'
            for j in range(24):
                exec(beep_on)
                GPIO.output(latch,0)
                GPIO.output(data_bit,int(bin[j])-1)
                GPIO.output(clock,1)
                GPIO.output(latch,1)
                GPIO.output(clock,0)
            exec(beep_off)
            wait(.5)            

        for i in range(lsb[1],msb[1]):
            bin=f'{i:b}'
            for j in range(24):
                exec(beep_on)
                GPIO.output(latch,0)
                GPIO.output(data_bit,int(bin[j]))
                GPIO.output(clock,1)
                GPIO.output(latch,1)
                GPIO.output(clock,0)
            exec(beep_off)
            wait(.5)
            
    except KeyboardInterrupt:
        exec(stop_program_message)
        
def binary_bits_inverse():
    
    try:    
        for i in range(msb[0],lsb[0],-1):
            bin=f'{i:b}'
            for j in range(24):
                exec(beep_on)
                GPIO.output(latch,0)
                GPIO.output(data_bit,int(bin[j]))
                GPIO.output(clock,1)
                GPIO.output(latch,1)
                GPIO.output(clock,0)
            exec(beep_off)
            wait(.5)            

        for i in range(lsb[1],msb[1]):
            bin=f'{i:b}'
            for j in range(24):
                exec(beep_on)
                GPIO.output(latch,0)
                GPIO.output(data_bit,int(bin[j])-1)
                GPIO.output(clock,1)
                GPIO.output(latch,1)
                GPIO.output(clock,0)
            exec(beep_off)
            wait(.5)
            
    except KeyboardInterrupt:
        exec(stop_program_message)
        
def binary_bits_mirror():
    
    try:    
        for i in range(msb[0],lsb[0],-1):
            bin=f'{i:b}'
            for j in range(23,-1,-1):
                exec(beep_on)
                GPIO.output(latch,0)
                GPIO.output(data_bit,int(bin[j])-1)
                GPIO.output(clock,1)
                GPIO.output(latch,1)
                GPIO.output(clock,0)
            exec(beep_off)
            wait(.5)            

        for i in range(lsb[1],msb[1]):
            bin=f'{i:b}'
            for j in range(23,-1,-1):
                exec(beep_on)
                GPIO.output(latch,0)
                GPIO.output(data_bit,int(bin[j]))
                GPIO.output(clock,1)
                GPIO.output(latch,1)
                GPIO.output(clock,0)
            exec(beep_off)
            wait(.5)
            
    except KeyboardInterrupt:
        exec(stop_program_message)        

def binary_bits_mirror_inverse():
    
    try:    
        for i in range(msb[0],lsb[0],-1):
            bin=f'{i:b}'
            for j in range(23,-1,-1):
                exec(beep_on)
                GPIO.output(latch,0)
                GPIO.output(data_bit,int(bin[j]))
                GPIO.output(clock,1)
                GPIO.output(latch,1)
                GPIO.output(clock,0)
            exec(beep_off)
            wait(.5)            

        for i in range(lsb[1],msb[1]):
            bin=f'{i:b}'
            for j in range(23,-1,-1):
                exec(beep_on)
                GPIO.output(latch,0)
                GPIO.output(data_bit,int(bin[j])-1)
                GPIO.output(clock,1)
                GPIO.output(latch,1)
                GPIO.output(clock,0)
            exec(beep_off)
            wait(.5)
            
    except KeyboardInterrupt:
        exec(stop_program_message)
        
def binary_bits_flow_default():
    
    try:    
        for i in range(msb[0],lsb[0],-1):
            bin=f'{i:b}'
            for j in range(24):
                GPIO.output(latch,0)
                GPIO.output(data_bit,int(bin[j])-1)
                GPIO.output(clock,1)
                GPIO.output(latch,1)
                GPIO.output(clock,0)
                wait(.05)            

        for i in range(lsb[1],msb[1]):
            bin=f'{i:b}'
            for j in range(24):
                GPIO.output(latch,0)
                GPIO.output(data_bit,int(bin[j]))
                GPIO.output(clock,1)
                GPIO.output(latch,1)
                GPIO.output(clock,0)
                wait(.05)
            
    except KeyboardInterrupt:
        exec(stop_program_message)
        
def binary_bits_flow_default_inverse():
    
    try:    
        for i in range(msb[0],lsb[0],-1):
            bin=f'{i:b}'
            for j in range(24):
                GPIO.output(latch,0)
                GPIO.output(data_bit,int(bin[j]))
                GPIO.output(clock,1)
                GPIO.output(latch,1)
                GPIO.output(clock,0)
                wait(.05)            

        for i in range(lsb[1],msb[1]):
            bin=f'{i:b}'
            for j in range(24):
                GPIO.output(latch,0)
                GPIO.output(data_bit,int(bin[j])-1)
                GPIO.output(clock,1)
                GPIO.output(latch,1)
                GPIO.output(clock,0)
                wait(.05)
            
    except KeyboardInterrupt:
        exec(stop_program_message)
        
binary_bits_trix=[
    binary_bits_default,
    binary_bits_inverse,
    binary_bits_mirror,
    binary_bits_mirror_inverse,
    binary_bits_flow_default,
    binary_bits_flow_default_inverse]

# Create an IndexError handler to
# cut off the buzzers, should you call
# an index value higher than [5].

# Note: index values always start at index zero
# not index one. Keep this in mind, should you
# accidentally call an index value higher than
# the index range.

try:
    binary_bits_trix[0]()
except IndexError:
    print('index value exceeds index range limit')

for i in range(24):            
    GPIO.output(latch,0)
    GPIO.output(data_bit,0)
    GPIO.output(clock,1)
    GPIO.output(latch,1)
    GPIO.output(clock,0)
    
GPIO.cleanup() # GPI.cleanup() sets all GPIO pins to LOW/OFF state
