# LCD Clock and Date Python program example:

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

# LCD clock and Date Python program example:

# This Raspberry Pi 4 Python program allows
# users to learn all about how the LCD display
# works with LCD clock and Date Python program.

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
from datetime import datetime
from time import sleep as wait

GPIO.setmode(GPIO.BOARD) # breadboard method
GPIO.setwarnings(False) # disable setwarnings
display=drivers.Lcd() # enable the LCD display

display.lcd_clear() # clear the LCD screen

# You can rename all these variables to any names you wish,
# but keep in mind that you must also rename any variables
# in your program as well. Click the Find and Replace command
# on the IDLE menu to make any renaming changes faster to cover
# any variables you want to rename. However, you should stick
# to meaningful names, so other programmers can learn and
# understand what's happening throughout the program's
# execution/run.

pause_delay=60

title=' RASPBERRY TIME '

stop_program_message='''
print('Stop program Execution/run:')
print('cleanup/release all GPIO pinouts \
to LOW state.')'''

# LCD Time Chars Guide:
# Do not remove any quote marks.

'''
LCD Time Chars

%l = 12 Hour
%H = 24 Hour
%M = Minute
%S = Second
%P = am/pm
%p = AM/PM

Do not remove any quote marks.
'''
# LCD Date Chars Guide:
# Do not remove any quote marks.

'''
LCD Date Chars

%A = Day of the Week long version
%a = Day of the Week short version
%B = Month long version
%b = Month short version
%e = Date
%Y = Year
%j = Days of Year
%U = Weeks of Year

Do not remove any quote marks.
'''

while True:
    try:
        display.lcd_clear()
        display.lcd_display_string(title,1)
        for i in range(pause_delay):
            gettime=datetime.now().strftime('%l:%M:%S %p')
            display.lcd_display_string(gettime,2)
            
        display.lcd_clear()
        display.lcd_display_string(title,1)
        for i in range(pause_delay):
            gettime=datetime.now().strftime(' %H:%M:%S')
            display.lcd_display_string(gettime,2)
            
        display.lcd_clear()
        display.lcd_display_string(title,1)
        for i in range(pause_delay):  
            display.lcd_display_string(' '+str(
                datetime.now().time()),2) # default time
            
        display.lcd_clear()
        display.lcd_display_string(title,1)
        for i in range(pause_delay):
            getdate=datetime.now().strftime('%a %b %e, %Y')
            display.lcd_display_string(getdate,2)
            
        display.lcd_clear()
        display.lcd_display_string(title,1)
        for i in range(pause_delay):
            getdate=datetime.now().strftime('Day %j, Week %U')
            display.lcd_display_string(getdate,2)
            
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
