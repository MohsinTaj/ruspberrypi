import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD) #physical pins selection
delayt=0.1
ldr=7
led=11
GPIO.setup(led,GPIO.OUT)




GPIO.