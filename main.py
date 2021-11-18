from flask import Flask, render_template
from yeelight import discover_bulbs
import json
from yeelight import discover_bulbs
from yeelight import Bulb


app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html",bulblist= discover_bulbs())

if __name__ == '__main__':
    app.run( host='0.0.0.0')