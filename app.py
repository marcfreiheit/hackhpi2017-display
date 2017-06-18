import bottle
from bottle import route, run, request, template, static_file, post, get
import os
import json
import led
import calibration


base_path = os.path.abspath(os.path.dirname(__file__))
view_path = os.path.join(base_path, 'views')
bottle.TEMPLATE_PATH.insert(0, view_path)

@route('/display/custom/<text>')
def do_display(text):
    led.displayInfo(text)

@route('/display/google')
def do_google():
    led.googleTest()

@route('/display/calibrate')
def do_calibration():
    led.calibrate()

run(host='172.16.63.40', port=8080, debug=True)