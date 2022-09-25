import RPi as GPIO #import raspiberry pi gpio pins
from time import sleep
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(7,GPIO.OUT,initial=GPIO.LOW)
while True:

    GPIO.output(8,GPIO.HIGH)
    GPIO.output(7,GPIO.LOW)
    sleep(1)
    GPIO.output(8,GPIO.LOW)
    GPIO.output(7,GPIO.HIGH)
    sleep(1)

