from subprocess import Popen
import subprocess
import time
import os
import signal
import sys

oilPumpProcess = subprocess.Popen(['python', 'oilPump.py', 'start'])
time.sleep(1)

#os.kill(oilPumpProcess.pid, signal.SIGTERM)

oilPumpProcess.kill()

subprocess.run(['python', 'oilPump.py', 'stop'])
