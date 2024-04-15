# 8b LCD Binary Counter Python program example:

# Created by Joseph C. Richardson, GitHub.com

# Note: be mindful while working with
# electronics. There are mistakes that
# cannot be corrected should you ignore
# any basic electronics rules. Electronics
# demands basic math skills and knowledge
# of electronics components alike.

# Items needed are as follows:

# Raspberry Pi = 1
# breadboard = 1 or more depending
# LCD display = 1
# 74HC595 shift register = 1
# LEDs = 8
# 220 ohm resistor = 8
# jumper wire = 20 or more +2 for the Rasp pi 4 fan

# Note: use two other jumper wires for
# the Raspberry Pi 4 fan, while in use/
# operation.

# 8b LCD Binary Counter Python program example:

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

import RPi.GPIO as GPIO,drivers
from time import sleep as wait

GPIO.setmode(GPIO.BOARD) # breadboard method
GPIO.setwarnings(False) # disable setwarnings
display=drivers.Lcd() # enable the LCD display

display.lcd_clear() # clear the LCD screen

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
msb=255,256 # most significant bits
lsb=127,128 # least significant bits

led_speed=.5 # pause duration

stop_program_message='''
print('Stop program Execution/run:')
print('cleanup/release all GPIO pinouts \
to LOW state.')'''

control_shift=data_bit,latch,clock

for i in control_shift:GPIO.setup(i,GPIO.OUT) # setup desired GPIO pinouts
    
for i in range(8):            
    GPIO.output(latch,0)
    GPIO.output(data_bit,0) # set all 8 data bits to 0/off
    GPIO.output(clock,1)    
    GPIO.output(latch,1)
    GPIO.output(clock,0)    

while True:    
    try:
        for i in range(msb[0],lsb[0],-1): # reverse forloop and step value -1
            display.lcd_display_string(
            f'Binary: {msb[0]-i:b}',1)
            display.lcd_display_string(
            f'Hex: {msb[0]-i:X} Dec: {msb[0]-i:d}',2)
            bin=f'{i:b}'
            for j in range(8):                
                GPIO.output(latch,0)
                GPIO.output(data_bit,int(bin[j])-1) # with 2's complement value -1
                GPIO.output(clock,1)
                GPIO.output(latch,1)
                GPIO.output(clock,0)                
            wait(led_speed)
            
        for i in range(lsb[1],msb[1]): # forward forloop
            display.lcd_display_string(
            f'Binary: {i:b}',1)
            display.lcd_display_string(
            f'Hex: {i:X} Dec: {i:d}',2)
            bin=f'{i:b}'
            for j in range(8):
                GPIO.output(latch,0)
                GPIO.output(data_bit,int(bin[j])) # without 2's complement
                GPIO.output(clock,1)
                GPIO.output(latch,1)
                GPIO.output(clock,0)
            wait(led_speed)
        break
            
# Note: it is recommended that you setup
# a KeyboardInterrupt handler to force
# the GPIO pins to return to a low state/off.

# GPIO.cleanup() sets all GPIO pins to LOW/OFF

    except KeyboardInterrupt:
        exec(stop_program_message) # GPIO notification message
        
        for i in range(8):            
            GPIO.output(latch,0)
            GPIO.output(data_bit,0) # set all 8 data bits to 0/off
            GPIO.output(clock,1)
            GPIO.output(latch,1)
            GPIO.output(clock,0)
            
        display.lcd_clear()
        display.lcd_backlight(0)
        GPIO.cleanup() # GPIO.cleanup() sets all GPIO pins to LOW/OFF
        break
