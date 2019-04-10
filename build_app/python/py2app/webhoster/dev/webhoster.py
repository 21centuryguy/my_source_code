
"""
https://www.bogotobogo.com/python/Bottle/Python_Bottle_Framework_static_files.php
"""

from tkinter import *
from tkinter import ttk
import os
from bottledaemon import daemon_run
from bottle import route, run, static_file, template
from threading import Thread


# ---------------------------------------
# -------- webhoster launcher  ----------
# ------------------------

def pass_host_port_from_gui():

    select_host_port_list = []

    # --- set root and frame
    root = Tk()
    root.title("WebHoster Launcher")
    frame = ttk.Frame(root, padding=8)

    # --- select host combo
    # - set combo itmes
    items = ['localhost', '172.20.10.2', '192.168.11.8']
    # - pass_selected_host
    def pass_selected_host(list, selected_item_num):
        selected_host = items[selected_item_num]
        print(selected_host)
        select_host_port_list.append(selected_host)
    # - combo box1
    cb_val = StringVar()
    cb_val.set("Select Host")
    cb = ttk.Combobox(frame, textvariable=cb_val, height=10, width=25)
    cb['values'] = items
    frame.grid()
    cb.grid(row=1, sticky=W)
    cb.bind('<<ComboboxSelected>>', lambda e:[pass_selected_host(items, int(cb.current()))])

    # --- select port combo
    # - set combo itmes
    items2 = ['1977', '1996', '1998', '2002', '2005', '2008', '2013', '2015', '2017', '2019']
    # - pass_selected_host
    def pass_selected_port(list, selected_item_num):
        selected_port = items2[selected_item_num]
        print(selected_port)
        select_host_port_list.append(selected_port)
    # - combo box2
    cb_val2 = StringVar()
    cb_val2.set("Select Port")
    cb2 = ttk.Combobox(frame, textvariable=cb_val2, height=10, width=25)
    cb2['values'] = items2
    frame.grid()
    cb2.grid(row=2, sticky=W)
    cb2.bind('<<ComboboxSelected>>', lambda e:[pass_selected_port(items2, int(cb2.current()))])

    # --- button for calling main func
    # -- func by button
    def save_selection():
        with open("tmp.py", "w") as f:
            f.write("select_host_port_list = ['")
            f.write(select_host_port_list[0])
            f.write("', ")
            f.write("'")
            f.write(select_host_port_list[1])
            f.write("']")

    # - button
    b1 = Button(frame, text="Submit", command=lambda:[save_selection(), quit()])
    frame.grid(); b1.grid(row=3, sticky=E);

    root.mainloop()

# -------------------------------------------------
# -------------------------------------
# -------------------------
# --------- webhoster

def webhoster():

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

    # -------------------------------
    # - call hoster
    # -------------------------------


    from tmp import select_host_port_list
    selected_host = select_host_port_list[0]
    selected_port = select_host_port_list[1]

    print("selected_host : ", selected_host)
    print("selected_port : ", selected_port)

    # -- run
    # run(host=selected_host, port=selected_port, debug=True) # home
   
    # -- run as deamon 
    # daemon_run(host=selected_host, port=selected_port)
    daemon_run(host="localhost", port="9999")



# ---------------------------------------
# -------- webhoster close  ----------
# ------------------------

def webhoster_closer():

    # --- set root and frame
    root2 = Tk()
    root2.title("WebHoster Closer")
    frame = ttk.Frame(root2, padding=8)

    # --- button for calling main func
    # - button
    b1 = Button(frame, text="Submit", command=lambda:[quit()])
    frame.grid(); b1.grid(row=1, sticky=E);

    root2.mainloop()



# ---------------------------------------
# -------- webhoster close  ----------
# ------------------------

# pass_host_port_from_gui()
webhoster()
# webhoster_closer()
