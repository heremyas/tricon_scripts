import RPi.GPIO as GPIO
import time
import grind.heavyForward as hf
import grind.heavyBackward as hb
import subprocess
import json

relay1 = 8 # Broadcom pin 18 (P1 pin 12)

def start():        
    hf.start()
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
                
                hxProcess = subprocess.Popen(['python', 'grind/hx711py/example.py'], stdout=subprocess.PIPE)
                  
                hb.start()    
               
                time.sleep(10) 
                out, err = hxProcess.communicate()

                GPIO.cleanup()  
                
                return(json.dumps({'msg': out.decode('utf-8')}))
                quit()
            
    except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
        GPIO.cleanup() # cleanup all GPIO
        

def stop():
    print("stop grinding")
    GPIO.cleanup() 

