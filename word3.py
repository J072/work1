import RPi.GPIO as GPIO
from flask import Flask
from flask import request
import threading
import time

app = Flask(__name__)

def job():
    global x
    while True:
        if x == 2:
            break
        
        GPIO.output(25, GPIO.HIGH)
        time.sleep(1)

        GPIO.output(25, GPIO.LOW)
        time.sleep(1)


@app.route('/',methods = ['GET'])

def index():
    global x
    led_status = request.args.get('led_status')
    
    if led_status == "0":
        x = 2
        GPIO.output(25, GPIO.LOW)
        return "LED_OFF"
        
    elif led_status == "1":
        x = 2
        GPIO.output(25, GPIO.HIGH)
        return "LED_ON"
    elif led_status == "2":
        x = 1
        t = threading.Thread(target = job)
        t.start()
        return "start"
    elif led_status == "3":
        x = 2
        return "stop"


if __name__ == '__main__':
    global x
    x = 1
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(25, GPIO.OUT)
    app.run()
    
