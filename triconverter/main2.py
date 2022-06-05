from flask import Flask
from flask_sock import Sock
from grinding import Grinding
from dehydrate import Dehydration
from testDht22 import Temp
import time

app = Flask(__name__)
sock = Sock(app)

grinder = Grinding()
dehydrateProcess = Dehydration()
tempSensor = Temp()


@sock.route('/temp')
def temp(ws):
    while True:
        
        #data = ws.receive()
        data = tempSensor.start() 
        print(data)
        #print(type(data), data)
        #if(type(data) != str):
        #    ws.send(data)
        ws.send(data) 
        
        time.sleep(1) 

@app.route("/dehydrate")
def dehydrate():    
    dehydrateProcess.start()
    return {"msg": "dehydrtion proces started"}

@app.route("/grind")
def grinding():    
    grinder.start()
    return {"msg": "dgrinder proces started"}

@app.route("/stop")
def stop():
    dehydrateProcess.stop()
    grinder.stop()
    return {"msg": "stopped"}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
