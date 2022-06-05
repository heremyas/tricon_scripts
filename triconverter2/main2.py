from flask import Flask
from flask_sock import Sock
import grind.grinding as gr
import dehydrate.dehydrate as dh
import testDht22 as dht
import time

app = Flask(__name__)
sock = Sock(app)

@sock.route('/temp')
def temp(ws):
    while True:
        
        #data = ws.receive()
        data = dht.start() 
        print(data)
        #print(type(data), data)
        #if(type(data) != str):
        #    ws.send(data)
        ws.send(data) 
        
        time.sleep(1) 

@app.route("/dehydrate")
def dehydrate():    
    dh.start()
    return {"msg": "dehydration started for 3 hours"}

@app.route("/grind")
def grinding():    
    data = gr.start()
    if(data):
        print(data)
        return data

@app.route("/stop")
def stop():
    dh.stop()
    gr.stop()
    return {"msg": "stopped"}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
