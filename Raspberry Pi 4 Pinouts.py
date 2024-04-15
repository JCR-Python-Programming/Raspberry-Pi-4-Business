# Note: be mindful while working with
# electronics. There are mistakes that
# cannot be corrected should you ignore
# any basic electronics rules. Electronics
# demands basic math skills and knowledge
# of electronics components alike.

# These are all the GPIO pins that you can use for lighting
# up LEDs or whatever devices that can 'safely' use these
# GPIO pins. I'm pretty new to using Raspberry Pi, I created
# these Cheat Sheets examples for quick references and
# understanding of the GPIO pin layout. My first Ras Pi
# project will envolve 10 red LEDs that will flash, flicker
# and chase one another using Python. So be looking out
# for this.

# (GPIO) General Purpose Input/Output: Pinouts

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)

GPIO.setup(27,GPIO.OUT) # GPIO 0
GPIO.setup(28,GPIO.OUT) # GPIO 1
GPIO.setup(3,GPIO.OUT) # GPIO 2
GPIO.setup(5,GPIO.OUT) # GPIO 3
GPIO.setup(7,GPIO.OUT) # GPIO 4
GPIO.setup(29,GPIO.OUT) # GPIO 5
GPIO.setup(31,GPIO.OUT) # GPIO 6
GPIO.setup(26,GPIO.OUT) # GPIO 7
GPIO.setup(24,GPIO.OUT) # GPIO 8
GPIO.setup(21,GPIO.OUT) # GPIO 9
GPIO.setup(19,GPIO.OUT) # GPIO 10
GPIO.setup(32,GPIO.OUT) # GPIO 12
GPIO.setup(33,GPIO.OUT) # GPIO 13
GPIO.setup(36,GPIO.OUT) # GPIO 16
GPIO.setup(11,GPIO.OUT) # GPIO 17
GPIO.setup(12,GPIO.OUT) # GPIO 18
GPIO.setup(35,GPIO.OUT) # GPIO 19
GPIO.setup(38,GPIO.OUT) # GPIO 20
GPIO.setup(40,GPIO.OUT) # GPIO 21
GPIO.setup(15,GPIO.OUT) # GPIO 22
GPIO.setup(16,GPIO.OUT) # GPIO 23
GPIO.setup(18,GPIO.OUT) # GPIO 24
GPIO.setup(22,GPIO.OUT) # GPIO 25
GPIO.setup(37,GPIO.OUT) # GPIO 26
GPIO.setup(13,GPIO.OUT) # GPIO 27

# Use these GPIO commands to turn GPIO pins ON or OFF

GPIO.output(7,GPIO.HIGH) # On
GPIO.output(7,GPIO.LOW) # Off

# Note: make sure to turn off all GPIO pins first before
# stopping any programs.

GPIO.cleanup() # Release all GPIO pins

# You can also use the Broadcom SOC Channel method
# if you prefer.

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

GPIO.setup(0,GPIO.OUT) # PIN 27
GPIO.setup(1,GPIO.OUT) # PIN 28
GPIO.setup(2,GPIO.OUT) # PIN 3
GPIO.setup(3,GPIO.OUT) # PIN 5
GPIO.setup(4,GPIO.OUT) # PIN 7
GPIO.setup(5,GPIO.OUT) # PIN 29
GPIO.setup(6,GPIO.OUT) # PIN 31
GPIO.setup(7,GPIO.OUT) # PIN 26
GPIO.setup(8,GPIO.OUT) # PIN 24
GPIO.setup(9,GPIO.OUT) # PIN 21
GPIO.setup(10,GPIO.OUT) # PIN 19
GPIO.setup(12,GPIO.OUT) # PIN 32
GPIO.setup(13,GPIO.OUT) # PIN 33
GPIO.setup(16,GPIO.OUT) # PIN 36
GPIO.setup(17,GPIO.OUT) # PIN 11
GPIO.setup(18,GPIO.OUT) # PIN 12
GPIO.setup(19,GPIO.OUT) # PIN 35
GPIO.setup(20,GPIO.OUT) # PIN 38
GPIO.setup(21,GPIO.OUT) # PIN 40
GPIO.setup(22,GPIO.OUT) # PIN 15
GPIO.setup(23,GPIO.OUT) # PIN 16
GPIO.setup(24,GPIO.OUT) # PIN 18
GPIO.setup(25,GPIO.OUT) # PIN 22
GPIO.setup(26,GPIO.OUT) # PIN 37
GPIO.setup(27,GPIO.OUT) # PIN 13

# Use these GPIO commands to turn GPIO pins ON or OFF

GPIO.output(4,GPIO.HIGH) # On
GPIO.output(4,GPIO.LOW) # Off

# Note: make sure to turn off all GPIO pins first before
# stopping any programs.

GPIO.cleanup() # Release all GPIO pins
