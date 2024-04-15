import time,RPi.GPIO as GPIO

buzzpin=11
GPIO.setmode(GPIO.BOARD)
GPIO.setup(buzzpin,GPIO.OUT)
buzz=GPIO.PWM(buzzpin,400)

buzz.start(50)

try:
    for i in range(5):    
        for x in range(50,1000):
            buzz.ChangeFrequency(x)
            time.sleep(.001)
        for x in range(1000,1,-1):
            buzz.ChangeFrequency(x)
            time.sleep(.001)
    buzz.stop(50)
    GPIO.cleanup()

except KeyboardInterrupt:
    GPIO.cleanup()
