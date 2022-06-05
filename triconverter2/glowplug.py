import RPi.GPIO as GPIO
import time

def start():
    # Pin Definitons:
    relay1 = 20 # Broadcom pin 18 (P1 pin 12)
    
    # Pin Setup:
    GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme
    GPIO.setup(relay1, GPIO.OUT) # LED pin set as output
    
    # Initial state for LEDs:
    GPIO.output(relay1, GPIO.LOW)
   
     
    t_end = time.time() + 60 * 60

    print("glow plug running")
    try:
        while (1): 
            if(time.time() < t_end):
                GPIO.output(relay1, GPIO.HIGH)
            else: 
                
                GPIO.cleanup()
                return True
    except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
        GPIO.cleanup() # cleanup all GPIO

def stop():
    GPIO.cleanup()

