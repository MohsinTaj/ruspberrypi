import RPi.GPIO as IO
import time
IO.setwarnings(False)
IO.setmode(IO.BCM)
IO.setup(2,IO.OUT)

IO.setup(3,IO.OUT)
IO.setup(14,IO.IN)
IO.setup(23 ,IO.IN,pull_up_down=IO.PUD_UP)
while 1:
    button=IO.input(23)
    if(IO.input(14)==True && button==False):
        IO.output(2,True)
        IO.output(3,False)
        
    if(IO.input(14)==False):
        IO.output(3,True)
        IO.output(2,False)    
