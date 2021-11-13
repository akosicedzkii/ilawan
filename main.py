from flask import Flask
from yeelight import discover_bulbs
import json

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>" + json.dumps(discover_bulbs())

if __name__ == '__main__':
    app.run( host='0.0.0.0')