from flask import Flask
from yeelight import discover_bulbs
import json
from yeelight import discover_bulbs
from yeelight import Bulb


app = Flask(__name__)

@app.route("/")
def hello_world():
    bulb = Bulb("192.168.1.3")
    #bulb.toggle()
    for a in json.dumps(discover_bulbs()):
        print(a)
    return "<p>Hello, World!</p>" 

if __name__ == '__main__':
    app.run( host='0.0.0.0')