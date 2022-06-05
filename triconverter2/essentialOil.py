import subprocess

from subprocess import Popen, PIPE

#peelWeightProcess = Popen(['python', 'hx711py/example.py'], stdout=PIPE, stderr=PIPE)
#stdout, stderr = peelWeightProcess.communicate()
#peelWeight = subprocess.run(['python', 'hx711py/example.py'], capture_output=True)

#convertedValue = float(peelWeight.stdout.decode("utf-8"))

print(f"you produced {convertedValue}. what do you want to do? \n 1 = mix essential oil, 2 = set aside powder.")

userChoice = int(input("enter number: "))

if userChoice == 1:
    cocoOilValue = convertedValue * 4.00   
    oilPumpProcess = subprocess.Popen(['python', 'oilPump.py'])
    cocoOilWeight = subprocess.run(['python', 'hx711py/forCocoOil.py', str(cocoOilValue)], capture_output=True) 
    oilPumpProcess.kill()
    print("done") 
        
elif userChoice == 2:
    print('please put the powder in the orange powder dispenser.')
    


