import RPi.GPIO as GPIO
import time

# Pin Definitons:
relay1 = 8 # Broadcom pin 18 (P1 pin 12)

# Pin Setup:
GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme
GPIO.setup(relay1, GPIO.OUT) # LED pin set as output

# Initial state for LEDs:
GPIO.output(relay1, GPIO.LOW)

t_end = time.time() + 60 * 180


try:
    while (1): 
        print("Grinding...")
        if(time.time() < t_end):
            GPIO.output(relay1, GPIO.HIGH)
        else:
            print('Grinder is resting for 10 seconds')
            time.sleep
except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
    GPIO.cleanup() # cleanup all GPIO

