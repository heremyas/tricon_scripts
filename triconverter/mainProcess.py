
from subprocess import Popen, PIPE


with Popen(['python', 'hx711py/exampleOrig.py'], stdout=PIPE, bufsize=1, universal_newlines=True) as p:
    for b in p.stdout:
        print(b, end='') # b is the byte from stdout

if p.returncode != 0:
    raise CalledProcessError(p.returncode, p.args)
#subprocess.run(['python', 'hx711py/exampleOrig.py'], capture_output=True)
    
 
