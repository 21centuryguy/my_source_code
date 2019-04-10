"""
https://www.bogotobogo.com/python/Bottle/Python_Bottle_Framework_static_files.php
"""

import os
from bottle import route, run, static_file, template

# root_path = os.getcwd() +"/"+ 'images' # directory path of target file
# root_path = os.getcwd() +"/"+ 'static' # directory path of target file
root_path = os.getcwd()

# --------------------------- pages
@route('/')
def serve_homepage():
    return template('webhoster.tpl')

@route('/page2')
def serve_homepage():
    return template('webhoster_2.tpl')

@route('/page3')
def serve_homepage():
    return template('webhoster_3.tpl')

@route('/page4')
def serve_homepage():
    return template('webhoster_4.tpl')

@route('/page5')
def serve_homepage():
    return template('webhoster_5.tpl')

@route('/page6')
def serve_homepage():
    return template('webhoster_6.tpl')

@route('/page7')
def serve_homepage():
    return template('webhoster_7.tpl')

@route('/page8')
def serve_homepage():
    return template('webhoster_8.tpl')

@route('/page9')
def serve_homepage():
    return template('webhoster_9.tpl')

@route('/page10')
def serve_homepage():
    return template('webhoster_10.tpl')


# --------------------------- static
@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root=root_path)

# --------------------------- run
# run(host='localhost', port=1977, debug=True)
run(host='172.20.10.2', port=1977, debug=True) # iphone 
# run(host='192.168.11.8', port=1977, debug=True) # home
