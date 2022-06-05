from flask import Flask
from flask_sock import Sock
from flask_restful import Resource, Api
from grinding import Grinding
from dehydrate import Dehydration

app = Flask(__name__)
sock = Sock(app)
grinder = Grinding()
dehydrateProcess = Dehydration()

api = Api(app)



ck.route('/echo')
def echo(ws):
    while True:
        data = ws.receive()
        ws.send(data)

class Dehydrate(Resource):
    def get(self):
        dehydrateProcess.start()

class Stop(Resource):
    def get(self):
        dehydrateProcess.stop()
        grinder.stop()

class Grind(Resource):
    def get(self):
        grinder.start()

api.add_resource(Dehydrate, '/dehydrate')
api.add_resource(Grind, '/grind')
api.add_resource(Stop, '/stop')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
