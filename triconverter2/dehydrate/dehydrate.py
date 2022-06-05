import RPi.GPIO as GPIO
import time


# Pin Definitons:
heaterBulb = 12 # Broadcom pin 18 (P1 pin 12)
heater = 7
heaterFan = 1

def start():     
    
    # Pin Setup:
    GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme
    GPIO.setup(heaterBulb, GPIO.OUT) # LED pin set as output
    GPIO.setup(heater, GPIO.OUT) # LED pin set as output
    GPIO.setup(heaterFan, GPIO.OUT) # LED pin set as output
    
    # Initial state for LEDs:
    GPIO.output(heaterBulb, GPIO.LOW)
    GPIO.output(heater, GPIO.LOW)
    GPIO.output(heaterFan, GPIO.LOW)
    
    
    t_end = time.time() + 60 * 180
    previous_time = 0
    
    print("Dehydrating process starting")
    
    try:
        print("Dehydrating for 3 hours")
        if(time.time() < t_end): 
            GPIO.output(heaterBulb, GPIO.HIGH) 
            GPIO.output(heater, GPIO.HIGH) 
            GPIO.output(heaterFan, GPIO.HIGH)
            time.time()
            

        else:
            print('Dehydration completed')
            return True
            GPIO.cleanup()
            quit()
    except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
        GPIO.cleanup() # cleanup all GPIO
def stop():
        
    GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme
    GPIO.setup(heaterBulb, GPIO.OUT) # LED pin set as output
    GPIO.setup(heater, GPIO.OUT) # LED pin set as output
    GPIO.setup(heaterFan, GPIO.OUT) # LED pin set as output
    
    GPIO.output(heaterBulb, GPIO.LOW)
    GPIO.output(heater, GPIO.LOW)
    GPIO.output(heaterFan, GPIO.LOW)

    GPIO.cleanup() 


#
#try:
#    while (1): 
#        print("Grinding...")
#        if(time.time() < t_end):
#            GPIO.output(relay1, GPIO.HIGH)
#        else:
#            print('Grinder is resting for 10 seconds')
#            time.sleep
#except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
#    GPIO.cleanup() # cleanup all GPIO

