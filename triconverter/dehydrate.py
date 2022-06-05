import RPi.GPIO as GPIO
import time

class Dehydration:
# Pin Definitons:
    heaterBulb = 12 # Broadcom pin 18 (P1 pin 12)
    heater = 7
    heaterFan = 1

    def start(self): 
        # Pin Setup:
        GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme
        GPIO.setup(self.heaterBulb, GPIO.OUT) # LED pin set as output
        GPIO.setup(self.heater, GPIO.OUT) # LED pin set as output
        GPIO.setup(self.heaterFan, GPIO.OUT) # LED pin set as output
        
        # Initial state for LEDs:
        GPIO.output(self.heaterBulb, GPIO.LOW)
        GPIO.output(self.heater, GPIO.LOW)
        GPIO.output(self.heaterFan, GPIO.LOW)
        
        
        t_end = time.time() + 60 * 180
        previous_time = 0
        
        print("Dehydrating process starting")
        
        try:
            print("Dehydrating for 3 hours")
            while (1):
                if(time.time() < t_end): 
                    GPIO.output(self.heaterBulb, GPIO.HIGH) 
                    GPIO.output(self.heater, GPIO.HIGH) 
                    GPIO.output(self.heaterFan, GPIO.HIGH)
                    time.time() 
                else:
                    print('Dehydration completed')
                    GPIO.cleanup()
                    quit()
        except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
            GPIO.cleanup() # cleanup all GPIO
    def stop(self):
        GPIO.output(self.heaterBulb, GPIO.LOW)
        GPIO.output(self.heater, GPIO.LOW)
        GPIO.output(self.heaterFan, GPIO.LOW)
    
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

