import RPi.GPIO as GPIO
import time 

out1 = 31
out2 = 35
out3 = 33
out4 = 37

i=0
positive=0
negative=0
y=0
speed=0.0008


GPIO.setmode(GPIO.BOARD)
GPIO.setup(out1,GPIO.OUT)
GPIO.setup(out2,GPIO.OUT)
GPIO.setup(out3,GPIO.OUT)
GPIO.setup(out4,GPIO.OUT)

print ("First calibrate by giving some +ve and -ve values.....")

x = -11000

try:
   #while(1):
   GPIO.output(out1,GPIO.LOW)
   GPIO.output(out2,GPIO.LOW)
   GPIO.output(out3,GPIO.LOW)
   GPIO.output(out4,GPIO.LOW)
   #if x>0 and x<=100:
   if x<0 and x>=-12000:
       x=x*-1
       for y in range(x,0,-1):
           if positive==1:
               if i==0:
                   i=7
               else:
                   i=i-1
               y=y+3
               positive=0
           negative=1
           #print((x+1)-y) 
           if i==0:
               GPIO.output(out1,GPIO.HIGH)
               GPIO.output(out2,GPIO.LOW)
               GPIO.output(out3,GPIO.LOW)
               GPIO.output(out4,GPIO.LOW)
               time.sleep(speed)
               #time.sleep(1)
           elif i==1:
               GPIO.output(out1,GPIO.HIGH)
               GPIO.output(out2,GPIO.HIGH)
               GPIO.output(out3,GPIO.LOW)
               GPIO.output(out4,GPIO.LOW)
               time.sleep(speed)
               #time.sleep(1)
           elif i==2:  
               GPIO.output(out1,GPIO.LOW)
               GPIO.output(out2,GPIO.HIGH)
               GPIO.output(out3,GPIO.LOW)
               GPIO.output(out4,GPIO.LOW)
               time.sleep(speed)
               #time.sleep(1)
           elif i==3:    
               GPIO.output(out1,GPIO.LOW)
               GPIO.output(out2,GPIO.HIGH)
               GPIO.output(out3,GPIO.HIGH)
               GPIO.output(out4,GPIO.LOW)
               time.sleep(speed)
               #time.sleep(1)
           elif i==4:  
               GPIO.output(out1,GPIO.LOW)
               GPIO.output(out2,GPIO.LOW)
               GPIO.output(out3,GPIO.HIGH)
               GPIO.output(out4,GPIO.LOW)
               time.sleep(speed)
               #time.sleep(1)
           elif i==5:
               GPIO.output(out1,GPIO.LOW)
               GPIO.output(out2,GPIO.LOW)
               GPIO.output(out3,GPIO.HIGH)
               GPIO.output(out4,GPIO.HIGH)
               time.sleep(speed)
               #time.sleep(1)
           elif i==6:    
               GPIO.output(out1,GPIO.LOW)
               GPIO.output(out2,GPIO.LOW)
               GPIO.output(out3,GPIO.LOW)
               GPIO.output(out4,GPIO.HIGH)
               time.sleep(speed)
               #time.sleep(1)
           elif i==7:    
               GPIO.output(out1,GPIO.HIGH)
               GPIO.output(out2,GPIO.LOW)
               GPIO.output(out3,GPIO.LOW)
               GPIO.output(out4,GPIO.HIGH)
               time.sleep(speed)
               #time.sleep(1)
           if i==0:
               i=7
               continue
           i=i-1 

   GPIO.cleanup()
              
except KeyboardInterrupt:
    GPIO.cleanup()
