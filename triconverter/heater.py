import RPi.GPIO as GPIO
import time

# Pin Definitons:
relay1 = 7 # Broadcom pin 18 (P1 pin 12)

# Pin Setup:
GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme
GPIO.setup(relay1, GPIO.OUT) # LED pin set as output

# Initial state for LEDs:
GPIO.output(relay1, GPIO.LOW)

print("Here we go! Press CTRL+C to exit")
try:
    while (1):
        GPIO.output(relay1, GPIO.HIGH) 
except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
    GPIO.cleanup() # cleanup all GPIO

