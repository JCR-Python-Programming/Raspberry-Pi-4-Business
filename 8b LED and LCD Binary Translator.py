# 8b LED and LCD Binary Translator Python program example:

# Created by Joseph C. Richardson, GitHub.com

# Note: be mindful while working with
# electroics. There are mistakes that
# cannot be corrected should you ignore
# any basic electronics rules. Electronics
# demands basic math skills and knowledge
# of electronics components alike.

# Items needed are as follows:

# Raspberry Pi 4 = 1
# breadboard = 1 # or more depending
# LCD display = 1
# 74HC595 shift register = 1
# LEDs = 8
# 220 ohm resistor = 8
# jumper wire = 20 or more +2 for the Rasp pi 4 fan

# Note: use two other jumper wires for
# the Raspberry Pi 4 fan, while in use/
# operation.

# 8b Binary Translator Python program example:

# This Raspberry Pi 4 Python program allows
# users to input decimal numbers, then
# translate them into binary, hexadecimal
# and decimal values using the 74HC595
# shift register.

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
# program example:

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
byte_range=256 # from 0 to 255

control_shift=data_bit,latch,clock

stop_program_message='''
print('Stop program Execution/run:')
print('cleanup/release all GPIO pinouts \
to LOW state.')'''

message='8B TRANSLATOR','ENTER 8B NUMBER:'
value_error='BYTE VALUES ONLY','PLEASE: 0-255'
index_error='VALUE EXCEEDS','8B RANGE 0-255'

for i in control_shift:GPIO.setup(i,GPIO.OUT)

for i in range(8):            
    GPIO.output(latch,0)
    GPIO.output(data_bit,0)
    GPIO.output(clock,1)
    GPIO.output(latch,1)
    GPIO.output(clock,0)
    
while True:
    try:
        while True:
            try:
                display.lcd_clear()
                display.lcd_display_string(
                message[0],1)
                byte=int(input(display.
                lcd_display_string(message[1],2)))
                if byte>=byte_range:
                    display.lcd_clear()
                    
                    for i in range(2):
                        display.lcd_display_string(
                        index_error[i],1+i)
                    wait(2)
                    break
                
                display.lcd_clear()
                display.lcd_display_string(
                f'BINARY: {byte:b}',1)
                display.lcd_display_string(
                f'HEX: {byte:X} DEC: {byte:d}',2)
                
                for i in range(byte,-1,-1):            
                    bin=f'{byte:b}'
                    for j in range(8):                
                        GPIO.output(latch,0)
                        GPIO.output(
                        data_bit,int(bin[j]))
                        GPIO.output(clock,1)
                        GPIO.output(latch,1)
                        GPIO.output(clock,0)
                            
            except ValueError:
                display.lcd_clear()
                for i in range(2):
                    display.lcd_display_string(
                    value_error[i],1+i)            
                wait(2)
                break
            
            except IndexError:
                pass
            wait(3)
            
            for i in range(8):            
                GPIO.output(latch,0)
                GPIO.output(data_bit,0)
                GPIO.output(clock,1)
                GPIO.output(latch,1)
                GPIO.output(clock,0)
            
# Note: it is recommended that you setup
# a KeyboardInterrupt handler to force
# the GPIO pins to return to a low state/off.

    except KeyboardInterrupt:
        exec(stop_program_message)
        
        for i in range(8):            
            GPIO.output(latch,0)
            GPIO.output(data_bit,0)
            GPIO.output(clock,1)
            GPIO.output(latch,1)
            GPIO.output(clock,0)
            
        display.lcd_clear()
        display.lcd_backlight(0)
        GPIO.cleanup() # GPIO.cleanup() sets all GPIO pins to LOW/OFF
        break
