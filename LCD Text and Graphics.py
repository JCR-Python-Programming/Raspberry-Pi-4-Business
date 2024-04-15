# LCD Text and Graphics Python program example:

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
# LCD display = 1
# jumper wire = 4 +2 for the Rasp pi 4 fan

# Note: use two other jumper wires for
# the Raspberry Pi 4 fan, while in use/
# operation.

# LCD Text and Graphics Python program example:

# This Raspberry Pi 4 Python program allows
# users to learn all about how the LCD display
# works with text and graphics.

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

c = drivers.CustomCharacters(display) # cannot rename

stop_program_message='''
print('Stop program Execution/run:')
print('cleanup/release all GPIO pinouts \
to LOW state.')'''
''''''''''''''''''''''''''''''
# Thise variables cannot be renamed;
# they are Python code only.

c.char_1_data=[
    '11111','10001',
    '10001','11111',
    '10000','10000',
    '10000','10000']

c.char_2_data=[
    '10001','10001',
    '10001','11111',
    '00001','00001',
    '10001','11111']

c.char_3_data=[
    '11111','00100',
    '00100','00100',
    '00100','00100',
    '00100','00100']

c.char_4_data=[
    '10001','10001',
    '10001','11111',
    '10001','10001',
    '10001','10001']

c.char_5_data=[
    '11111','10001',
    '10001','10001',
    '10001','10001',
    '10001','11111']

c.char_6_data=[
    '10001','11001',
    '10101','10011',
    '10001','10001',
    '10001','10001']

c.char_7_data=[
    '11110','11010',
    '00010','11111',
    '11111','01000',
    '01011','01111']
''''''''''''''''''''''''''''''
while True:
    try:
        c.load_custom_characters_data()
        display.lcd_display_extended_string(
        ' '*3+'{0x06} {0x00}{0x01}{0x02}{0x03}{0x04}{0x05} {0x06}',1)
        display.lcd_display_extended_string(' Python is fun!',2)

# Note: it is recommended that you setup
# a KeyboardInterrupt handler to force
# the GPIO pins to return to a low state/off.

# GPIO.cleanup() sets all GPIO pins to LOW/OFF

    except KeyboardInterrupt:
        exec(stop_program_message) # GPIO notification message
        display.lcd_clear()
        display.lcd_backlight(0)
        GPIO.cleanup() # GPIO.cleanup() sets all GPIO pins to LOW/OFF
        break
