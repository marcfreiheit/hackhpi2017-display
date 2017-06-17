import bottle
from bottle import route, run, request, template, static_file, post, get
import os
import json
import child-growth-info

base_path = os.path.abspath(os.path.dirname(__file__))
view_path = os.path.join(base_path, 'views')
bottle.TEMPLATE_PATH.insert(0, view_path)

@route('/display/<text>')
def do_display(text):
    child-growth-info.displayInfo(text)

run(host='localhost', port=8080, debug=True)