import bottle
from bottle import route, run, request, template, static_file, post, get
import os
import json
import led

base_path = os.path.abspath(os.path.dirname(__file__))
view_path = os.path.join(base_path, 'views')
bottle.TEMPLATE_PATH.insert(0, view_path)

@route('/display/<text>')
def do_display(text):
    led.displayInfo(text)

run(host='172.16.63.40', port=8080, debug=True)