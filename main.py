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
    htmlcode = ""
    for a in discover_bulbs():
        print(a)
        htmlcode = htmlcode + "<h3>" + a["ip"] + "</h3><br>"
    return htmlcode

if __name__ == '__main__':
    app.run( host='0.0.0.0')