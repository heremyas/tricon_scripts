import subprocess
import time
from subprocess import Popen, PIPE
import os
import signal

#peelWeightProcess = Popen(['python', 'hx711py/example.py'], stdout=PIPE, stderr=PIPE)
#stdout, stderr = peelWeightProcess.communicate()

print('load sensor initializing...')
peelWeight = subprocess.Popen(['python', 'hx711py/example.py'], stdout=PIPE)

time.sleep(3)

forWeighing = subprocess.Popen(['python', 'heavyBackward.py'])

out, err = peelWeight.communicate()

convertedValue = float(out.decode("utf-8"))

print(f"you produced {convertedValue}. what do you want to do? \n 1 = mix essential oil, 2 = set aside powder.")

userChoice = int(input("enter number: "))

if userChoice == 1:
    cocoOilValue = convertedValue * 4.00   
    oilPumpProcess = subprocess.Popen(['python', 'oilPump.py', 'start'])
    cocoOilWeight = subprocess.run(['python', 'hx711py/forCocoOil.py', str(cocoOilValue)], capture_output=True) 
    #os.killpg(os.getpgid(oilPumpProcess.pid), signal.SIGTERM)
    
    oilPumpProcess.kill() 
    subprocess.run(['python', 'oilPump.py', 'stop']) 
    print("done") 
        
elif userChoice == 2:
    print('please put the powder in the orange powder dispenser.')
    


