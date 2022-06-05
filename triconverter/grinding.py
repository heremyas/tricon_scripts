import RPi.GPIO as GPIO
import time


relay1 = 8 # Broadcom pin 18 (P1 pin 12)



def start():        
    import heavyForward
    time.sleep(3)
    # Pin Setup:
    GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme
    GPIO.setup(relay1, GPIO.OUT) # LED pin set as output
    
    # Initial state for LEDs:
    GPIO.output(relay1, GPIO.LOW)
    t_end = time.time() + 60 * .1
    print("Grinding...")
    try:
        while (1): 
            if(time.time() < t_end):
                GPIO.output(relay1, GPIO.HIGH)
            else: 
                GPIO.output(relay1, GPIO.LOW)
                print('Grinder is resting for 10 seconds')
                time.sleep(3)
                GPIO.cleanup() 
                
                print("grinding finished") 
                import heavyBackward 
                GPIO.cleanup()  
                quit()
            
    except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
        GPIO.cleanup() # cleanup all GPIO
        

def stop():
    print("stop grinding")
    GPIO.cleanup() 

