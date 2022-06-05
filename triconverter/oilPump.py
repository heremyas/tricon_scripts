import RPi.GPIO as GPIO          
import signal
import sys
from time import sleep

in1 = 11
in2 = 9

GPIO.setmode(GPIO.BCM)
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)

GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)

if(sys.argv[1] == 'stop'):
    GPIO.cleanup()
else:
    try:
        while(1):
            GPIO.output(in1, GPIO.HIGH)
            GPIO.output(in2, GPIO.LOW)
    
    
    except KeyboardInterrupt or SystemExit:
        GPIO.cleanup()
    
