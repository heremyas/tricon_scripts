import RPi.GPIO as GPIO          
from time import sleep

in1 = 21
in2 = 5

GPIO.setmode(GPIO.BCM)
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)

GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)

try:
    while(1):
        GPIO.output(in1, GPIO.HIGH)
        GPIO.output(in2, GPIO.LOW)
except KeyboardInterrupt:
    GPIO.cleanup()
