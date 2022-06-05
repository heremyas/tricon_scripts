# PDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import time
import board
import adafruit_dht
import json

# Initial the dht device, with data pin connected to:

class Temp:
    dhtDevice = adafruit_dht.DHT22(board.D18, use_pulseio=False)
    
    
    # you can pass DHT22 use_pulseio=False if you wouldn't like to use pulseio.
    # This may be necessary on a Linux single board computer like the Raspberry Pi,
    # but it will not work in CircuitPython.
    # dhtDevice = adafruit_dht.DHT22(board.D18, use_pulseio=False)
        
    def start(self): 
        try:
            # Print the values to the serial port
            temperature_c = self.dhtDevice.temperature
            if(temperature_c):
                temperature_f = temperature_c * (9 / 5) + 32
                humidity = self.dhtDevice.humidity
                return(json.dumps({'temp': temperature_c, 'humid': humidity}))
            else:
                return(json.dumps({}))
                #return("Temp: {:.1f} F / {:.1f} C    Humidity: {}% ".format(temperature_f, temperature_c, humidity))    
        #except RuntimeError as error:
        #    # Errors happen fairly often, DHT's are hard to read, just keep going
        #    print(error.args[0])
        #    time.sleep(2.0)
        #    continue
        #except Exception as error:
        #    self.dhtDevice.exit()
        #    raise error
        #except KeyboardInterrupt:
        #    self.dhtDevice.exit()     
        except RuntimeError as e:
            return (json.dumps({}))
            
    def stop(self):
        self.dhtDevice.exit()
