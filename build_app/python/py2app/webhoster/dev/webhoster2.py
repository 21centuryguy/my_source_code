
"""
https://www.bogotobogo.com/python/Bottle/Python_Bottle_Framework_static_files.php
"""

from tkinter import *
from tkinter import ttk
import os
from bottledaemon import daemon_run
from bottle import route, run, static_file, template

# root_path = os.getcwd() +"/"+ 'images' # directory path of target file
# root_path = os.getcwd() +"/"+ 'static' # directory path of target file
root_path = os.getcwd() + "/"

# --------------------------- pages

@route("/")
def serve_homepage():
    return template(root_path + "webhoster.tpl")

@route("/page2")
def serve_homepage():
    return template(root_path + "webhoster_2.tpl")

@route("/page3")
def serve_homepage():
    return template(root_path + "webhoster_3.tpl")

@route("/page4")
def serve_homepage():
    return template(root_path + "webhoster_4.tpl")

@route("/page5")
def serve_homepage():
    return template(root_path + "webhoster_5.tpl")

@route("/page6")
def serve_homepage():
    return template(root_path + "webhoster_6.tpl")

@route("/page7")
def serve_homepage():
    return template(root_path + "webhoster_7.tpl")

@route("/page8")
def serve_homepage():
    return template(root_path + "webhoster_8.tpl")

@route("/page9")
def serve_homepage():
    return template(root_path + "webhoster_9.tpl")

@route("/page10")
def serve_homepage():
    return template(root_path + "webhoster_10.tpl")

# --------------------------- static
@route("/static/<filepath:path>")
def server_static(filepath):
    return static_file(filepath, root=root_path)

# -------------------------------
# - call hoster
# -------------------------------


from tmp import select_host_port_list
selected_host = select_host_port_list[0]
selected_port = select_host_port_list[1]

# print("selected_host : ", selected_host)
# print("selected_port : ", selected_port)

# -- run
# run(host=selected_host, port=selected_port, debug=True) # home
# run(host="localhost", port="8888", debug=False) # home
daemon_run(host="localhost", port="7777")
