import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setmode(23,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(24,GPIO.OUT)
try:
    while True:
        button_state=GPIO.input(23)
        if button_state==false:
            GPIO.output(24,True)
            print('button pressed')
                time.sleep(0.2)
        else:
            GPIO.output(24,False)
            
except:
    GPIO.cleanup()