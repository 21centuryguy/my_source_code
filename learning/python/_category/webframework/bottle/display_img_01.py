"""
https://www.bogotobogo.com/python/Bottle/Python_Bottle_Framework_static_files.php
"""

from bottle import route, run, static_file, template

HOST = 'localhost'

@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='images/')

@route('/')
def serve_homepage():
    return template('display_img_01.tpl')

run(host='localhost', port=8080, debug=True)
# run(host='172.20.10.2', port=8080, debug=True)