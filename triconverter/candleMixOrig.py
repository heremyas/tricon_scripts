import subprocess
from subprocess import PIPE
import time

candleCount = int(input("how many candle/s do you wan to produce?"))

# for example user chose 1
wax = 70
oil = 20

print('initializing load sensor')
candleProcess = subprocess.Popen(['python','hx711py/example.py', str(wax * candleCount)], stdout=PIPE)
time.sleep(3)


print('wax dispenser active')
dispenserProcess = subprocess.Popen(['python', 'waxDispenser.py', 'start'])

out, err = candleProcess.communicate()

if(out):
    print('done')
    dispenserProcess.kill()
    subprocess.Popen(['python', 'waxDispenser.py', 'stop'])
    








