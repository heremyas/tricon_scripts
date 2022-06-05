import RPi.GPIO as GPIO

in1 = 3
in2 = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.output(in1,GPIO.HIGH)
GPIO.output(in2,GPIO.HIGH)
