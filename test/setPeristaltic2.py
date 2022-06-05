import RPi.GPIO as GPIO

out1 = 3
out2 = 4
out3 = 3
out4 = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(out1,GPIO.OUT)
GPIO.setup(out2,GPIO.OUT)
GPIO.setup(out3,GPIO.OUT)
GPIO.setup(out4,GPIO.OUT)

try: 
    while(1):
        GPIO.output(out1,GPIO.LOW)
        GPIO.output(out2,GPIO.LOW)
        GPIO.output(out3,GPIO.LOW)
        GPIO.output(out4,GPIO.LOW)

except KeyboardInterrupt:
    GPIO.cleanup()
    
     
