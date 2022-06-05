import multiprocessing as mp
import example as ls
import waxDispenser as wd
import heavyForward as hf
import glowplug as gp
from time import sleep
import sys

def loadSensor(loadSensorQueue): 
    try:     
        while True:
            loadSensorQueue.put(ls.start())
            sleep(.1)
    except KeyboardInterrupt:
        ls.stop()

def pourWax():
    try:
        wd.start() 
    except KeyboardInterrupt:
        wd.stop()

def moveToRight():
    try:
        hf.start()
    except KeyboardInterrupt:
        hf.stop()

def glowPlug():
    try:
        gp.start()
    except KeyboardInterrupt:
        gp.stop()

if __name__ == '__main__': 
    loadSensorQueue = mp.Queue()

    loadSensorProcess = mp.Process(target=loadSensor, args=(loadSensorQueue, ))
    pourWaxProcess = mp.Process(target=pourWax)
    moveRightProcess = mp.Process(target=moveToRight)
    glowPlugProcess = mp.Process(target=glowPlug)

    loadSensorProcess.start()
    pourWaxProcess.start()

    while True: 
        print(loadSensorQueue.get())
        if(loadSensorQueue.get() >= 80):
           
            wd.stop() 
            pourWaxProcess.terminate()
            break
  
    print('glow plug start')
    glowPlugProcess.start() 

    sleep(3)
    # moverightprocess end
    moveRightProcess.start()
    moveRightProcess.join() 
    
    print('move right process done')
    sleep(2)
    
       
    print('Process end') 
    sys.exit() 
   
