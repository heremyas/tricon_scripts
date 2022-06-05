
from __future__ import print_function # Only Python 2.x
import subprocess

def execute(cmd):
    popen = subprocess.Popen(['python', 'hx711py/exampleOrig.py'], stdout=subprocess.PIPE, universal_newlines=True)
    for stdout_line in iter(popen.stdout.readline, ""):
        yield stdout_line 
    popen.stdout.close()
    return_code = popen.wait()
    if return_code:
        raise subprocess.CalledProcessError(return_code, cmd)

# Example

for path in execute(["python", "hx711py/exampleOrig.py"]):
    print('hello')
    print(path, end="")
