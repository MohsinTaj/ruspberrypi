import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD) #physical pins selection
delayt=0.1
value=0
ldr=7
led=11
GPIO.setup(led,GPIO.OUT)
GPIO.output(led,False)
def rc_time(ldr):
    
    count=0
    GPIO.setup(ldr,GPIO.OUT)
    GPIO.output(ldr,False)
    time.sleep(delayt)
    
    
    GPIO.setup(ldr,GPIO.IN)
    while(GPIO.input(ldr)==0):
        count+=1
    return count



try:
    while 1:
        print("ldr value")
        value=rc_time(ldr)
        print(value)
        if (value<=10000):
            print("lights are on")
            GPIO.output(led,True)
        if(value>10000):
            print("light are OFF")
            GPIO.output(led,False)
            
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()
    