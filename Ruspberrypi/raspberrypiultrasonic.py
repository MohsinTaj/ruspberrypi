 import RPi.GPIO as IO
 import time
 IO.setmode(GPIO.BCM)
 TRIG=2
 ECHO=3
 print("Distance measurement in progress")
 IO.setup(TRIG,IO.OUT)
 IO.setup(ECHO,IO.IN)
 while 1:
     IO.output(TRIG,False)
     print("waiting for sensor to settle")
     IO.output(TRIG,False)
     
 while IO.input(ECHO)==0:
     pulse_start=time.time()
 
 while IO.input(ECHO)==1:
     pulse_end=time.time()
     
 pulse_duration=pulse_end-pulse_start
 
 
 distance=pulse_duration*17150
 
 distance=round(distance,2)
 if distance>2 and distance<400:
     print("distance : "distance-0.5, "cm")
     
 else:
     print("out of range")