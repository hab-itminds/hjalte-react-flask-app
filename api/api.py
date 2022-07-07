import time
from flask import Flask
import requests


app = Flask(__name__)

@app.route('/time')
def get_current_time():
    return {'time': time.time()}

@app.route('/feriecamp')
def get_feriecamp_data():
    req = requests.get('https://feriecamp.kk.dk/api/event')
    return req.text