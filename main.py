import atexit
import os

from flask import Flask, send_file
from flask_socketio import SocketIO
# from adafruit_motorkit import MotorKit

isRaspberryPi = os.path.isfile('/etc/os-release')

# Define Motor Aliases
# kit = MotorKit()

# leftH = kit.motor1
# rightH = kit.motor2
# leftV = kit.motor3
# rightV = kit.motor4
    
# Controller
app = Flask(__name__, static_folder="static")
socketio = SocketIO(app)

@app.route('/')
def index():
    return send_file('index.html')

@socketio.on('drive')
def drive(state):
    pass
    # leftH.throttle = state['horizontal'][0]
    # rightH.throttle = state['horizontal'][1]
    # leftV.throttle = state['vertical']
    # rightV.throttle = state['vertical']

socketio.run(app, host='0.0.0.0', port=8080, debug=not isRaspberryPi)

@atexit.register
def cleanup():
    print('Clean exit')