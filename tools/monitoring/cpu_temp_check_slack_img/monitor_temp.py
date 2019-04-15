# -*- coding: utf-8 -*-

import os
import time
from time import localtime, strftime
import requests
import json
import numpy as np
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
from PIL import Image

# --------------------------
# --- func definition

def measure_temp():
    temp = os.popen("vcgencmd measure_temp").readline()
    temp = temp.replace("temp=", "")
    temp = temp.replace("'C", "")
    with open(temp_log_file_full_path, "a+") as f:
        f.write(temp)
    return temp

def create_temp_graph():
    f = open(temp_log_file_full_path, mode="r")
    temp_list = f.read().splitlines()

    figure(num=None, figsize=(30, 10), dpi=80, facecolor='w', edgecolor='k')

    i = 0
    x = list()
    y = list()
    for temp in temp_list:
        i = i + 1
        x.append(i)
        y.append(float(temp))

    plt.scatter(x, y)
    plt.plot(x, y)
    plt.title('Raspbery CPU Temp Graph', fontsize = 70)
    plt.xlabel('Temp Measure Count(/ 1min)', fontsize = 30)
    plt.ylabel("CPU Temp ('C)", fontsize = 30) 
    plt.savefig(temp_image_full_path)
    # plt.show()

def post_a_message_to_slack(requests_post_url, channel_name, poster_name, message_text, poster_icon):
    def create_json_message(channel_name, poster_name, message_text, poster_icon):
        json_message = {"channel": channel_name, "username": poster_name, "text": message_text, "icon_emoji": poster_icon}
        return json_message

    def post_json_message_to_slack(requests_post_url, json_message):
        response = requests.post(requests_post_url, json=json_message)
        # print("message posting response :", response.status_code)

    json_message = create_json_message(channel_name, poster_name, message_text, poster_icon)
    # print("json_message : ", json_message)

    post_json_message_to_slack(requests_post_url, json_message)

def resize_image_file_size():
    foo = Image.open(temp_image_full_path) # 72kb
    foo = foo.resize((1200,400),Image.ANTIALIAS)
    foo.save(temp_image_full_path, quality=100) # 2

def post_a_file_to_slack(file_full_path, channel_id, your_token):
    files = {'file': open(file_full_path, 'rb')}
    param = {'token':your_token, 'channels':channel_id}
    response = requests.post(url="https://slack.com/api/files.upload", params=param, files=files)
    # print("files posting response :", response.status_code)


# ---------------------------
# --- var

# - info for post message
requests_post_url = "YOUR WEBHOOK URL"
channel_name = 'respberry_raspbian'
poster_name = 'pyscript_on_py'
poster_icon = 'simple_smile'

# - info for post file
channel_id = 'YOUR CHANNEL ID'
your_token = 'YOUR WORKSAPCE TOKEN'

# - file path
log_folder_path = "/usr/local/bin/log/"
temp_log_file_name = "temp_log.txt"
temp_log_file_full_path = log_folder_path + temp_log_file_name

image_folder_path = "/usr/local/bin/image/"
temp_image_file_name = "temp_graph.png"
temp_image_full_path = image_folder_path + temp_image_file_name



# ---------------------------
# --- call

check_temp_time = strftime("%Y-%m-%d %H:%M:%S", localtime())
current_temp = measure_temp()
    
# ---
# print("="*33)
# print(check_temp_time)
# print(current_temp)
    
# ---
message_text = "="*33 + "\n" + str(check_temp_time) + "\n" + str(current_temp) + "\n"
post_a_message_to_slack(requests_post_url, channel_name, poster_name, message_text, poster_icon)

# ---
create_temp_graph()

#---
resize_image_file_size()

# ---
post_a_file_to_slack(temp_image_full_path, channel_id, your_token)

