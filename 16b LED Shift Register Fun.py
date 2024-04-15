# 16b LED Shift Register Fun Python program example:

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
# jumper wire = 38 or more +2 for the Rasp pi 4 fan

# Note: use two other jumper wires for
# the Raspberry Pi 4 fan, while in use/
# operation.

# 16b Shift Register Fun Python program example:

# This Raspberry Pi 4 Python program allows
# users to have tons of fun, while learning
# how two 8b 74HC595 shift registers work.

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
led_speed=.1 # pause duration

stop_program_message='''
print('Stop program Execution/run:')
print('cleanup/release all GPIO pinouts \
to LOW state.')'''

control_shift=data_bit,latch,clock

for i in control_shift:GPIO.setup(i,GPIO.OUT) # setup desired GPIO pinouts

on_off=[
    '1111111111111111','0000000000000000','1111111111111111','0000000000000000',
    '1111111111111111','0000000000000000']

single_pass=[
    '1000000000000001','0100000000000010','0010000000000100','0001000000001000',
    '0000100000010000','0000010000100000','0000001001000000','0000000110000000',       
    '0000001001000000','0000010000100000','0000100000010000','0001000000001000',
    '0010000000000100','0100000000000010']

double_pass=[
    '1000000000000001','1100000000000011','0110000000000110','0011000000001100',
    '0001100000011000','0000110000110000','0000011001100000','0000001111000000',
    '0000000110000000','0000001111000000','0000011001100000','0000110000110000',
    '0001100000011000','0011000000001100','0110000000000110','1100000000000011']

triple_pass=[
    '1000000000000001','1100000000000011','1110000000000111','0111000000001110',
    '0011100000011100','0001110000111000','0000111001110000','0000011111100000',
    '0000001111000000','0000000110000000','0000001111000000','0000011111100000',
    '0000111001110000','0001110000111000','0011100000011100','0111000000001110',
    '1110000000000111','1100000000000011']

single_right=[
    '1001001001001001','0100100100100100','0010010010010010']

single_left=[
    '1001001001001001','0010010010010010','0100100100100100']

double_right=[
    '1100110011001100','0110011001100110','0011001100110011','1001100110011001']

double_left=[
    '0011001100110011','0110011001100110','1100110011001100','1001100110011001']

join_inward=[
    '1000000000000001','1100000000000011','1110000000000111','1111000000001111',
    '1111100000011111','1111110000111111','1111111001111111','1111111111111111']

split_outward=[
    '1111111001111111','1111110000111111','1111100000011111','1111000000001111',
    '1110000000000111','1100000000000011','1000000000000001']    
    
collapse_inward=[
    '0111111111111110','0011111111111100','0001111111111000','0000111111110000',
    '0000011111100000','0000001111000000','0000000110000000']

expand_outward=[
    '0000001111000000','0000011111100000','0000111111110000','0001111111111000',
    '0011111111111100','0111111111111110','1111111111111111']

stack_inward=[
    '0100000000000010','0010000000000100','0001000000001000','0000100000010000',
    '0000010000100000','0000001001000000','0000000110000000','1000000110000001',
    '0100000110000010','0010000110000100','0001000110001000','0000100110010000',
    '0000010110100000','0000001111000000','1000001111000001','0100001111000010',
    '0010001111000100','0001001111001000','0000101111010000','0000011111100000',
    '1000011111100001','0100011111100010','0010011111100100','0001011111101000',
    '0000111111110000','1000111111110001','0100111111110010','0010111111110100',
    '0001111111111000','1001111111111001','0101111111111010','0011111111111100',
    '1011111111111101','0111111111111110','1111111111111111']

stack_outward=[
    '0000001001000000','0000010000100000','0000100000010000','0001000000001000',
    '0010000000000100','0100000000000010','1000000000000001','1000000110000001',
    '1000001001000001','1000010000100001','1000100000010001','1001000000001001',
    '1010000000000101','1100000000000011','1100000110000011','1100001001000011',
    '1100010000100011','1100100000010011','1101000000001011','1110000000000111',
    '1110000110000111','1110001001000111','1110010000100111','1110100000010111',
    '1111000000001111','1111000110001111','1111001001001111','1111010000101111',
    '1111100000011111','1111100110011111','1111101001011111','1111110000111111',
    '1111110110111111','1111111001111111','1111111111111111']

flash_dance=[
    '1100000000000011','0000000110000000','1100000000000011','0000000110000000',
    '1100000000000011','0000000110000000','1100000000000011','0000000110000000']    

flip_flop=[
    '1111111100000000','0000000011111111','1111111100000000','0000000011111111',
    '1111111100000000','0000000011111111']

led_follow_right=[
    '0111111100111111','0011111110011111','1001111111001111','1100111111100111',
    '1110011111110011','1111001111111001','1111100111111100','1111110011111110']

led_follow_left=[
    '1111110011111110','1111100111111100','1111001111111001','1110011111110011',
    '1100111111100111','1001111111001111','0011111110011111','0111111100111111']

variable_array=[on_off,
    single_pass,double_pass,
    triple_pass,join_inward,
    collapse_inward,stack_outward,
    split_outward,stack_inward,
    collapse_inward,flip_flop,
    led_follow_left,flip_flop,
    led_follow_right,flash_dance]

for i in range(16):            
    GPIO.output(latch,0)
    GPIO.output(data_bit,0)
    GPIO.output(clock,1)
    GPIO.output(latch,1)
    GPIO.output(clock,0)

while True:
    try:
        for x in range(15):
            for i in variable_array[x]:
                for j in range(16):               
                    GPIO.output(latch,0)
                    GPIO.output(data_bit,int(i[j]))
                    GPIO.output(clock,1)
                    GPIO.output(latch,1)
                    GPIO.output(clock,0)
                wait(led_speed)
                
        for i in range(16):            
            GPIO.output(latch,0)
            GPIO.output(data_bit,0)
            GPIO.output(clock,1)
            GPIO.output(latch,1)
            GPIO.output(clock,0)
        GPIO.cleanup()
        break
            
# Note: it is recommended that you setup
# a KeyboardInterrupt handler to force
# the GPIO pins to return to a low state/off.

# GPIO.cleanup() sets all GPIO pins to LOW/OFF

    except KeyboardInterrupt:
        exec(stop_program_message) # GPIO notification message
        
        for i in range(16):            
            GPIO.output(latch,0)
            GPIO.output(data_bit,0)
            GPIO.output(clock,1)
            GPIO.output(latch,1)
            GPIO.output(clock,0)
        GPIO.cleanup()
        break
