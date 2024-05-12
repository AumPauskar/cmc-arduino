from flask import Flask
from flask import render_template
from flask import request
import RPi.GPIO as GPIO
import time
import subprocess

# global constants
on_temp = 65
off_temp = 55
gpio = 17
enable = 27

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(gpio, GPIO.OUT)
GPIO.setup(enable, GPIO.OUT)
pwm = GPIO.PWM(enable, 100)
pwm.start(100)

app = Flask(__name__)

@app.route('/')
def html_page():
    return render_template('index.html')

@app.route('/send', methods=['POST'])
def send():
    number_input = request.form.get('numberInput', '')
    # Use the 'number' variable for further processing
    rotate_fan(int(number_input))
    return 'Received number: ' + number_input

def rotate_fan(specified_time):
    GPIO.output(gpio, GPIO.HIGH)
    time.sleep(specified_time)
    GPIO.output(gpio, GPIO.LOW)
    
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
