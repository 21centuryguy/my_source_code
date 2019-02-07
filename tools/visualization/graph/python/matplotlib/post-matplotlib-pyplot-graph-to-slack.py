import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import requests

#########################################################################################
### GLOBAL VARIABLES

#######################################
############### slack receiver url, token, channles

#### xxx
xxx_channel_info = {
'requests_post_url':'xxx',
'token':'xxx',
'channels':'xxx'}

#### mirai_incident
xxx_channel_info = {
'requests_post_url':'xxx',
'token':'xxx',
'channels':'xxx'}

#### jack direct
xxx_channel_info = {
'requests_post_url':'xxx',
'token':'xxx',
'channels':'xxx'}


xxx_log_folder_path = "xxx"
xxx_log_file_name = "xxx.txt"
xxx_log_file_full_path = xxx_log_folder_path + xxx_log_file_name

screenshot_folder_path = "xxx"
screenshot_file_name = "xxx.png"
screenshot_file_full_path = screenshot_folder_path + screenshot_file_name

### GLOBAL VARIABLES
#########################################################################################
### FUNC DEFINITION


#######################################
############ func definition

def create_filetrans_time_graph():

    f = open(time_log_file_full_path, mode="r")
    filetrans_time_list = f.read().splitlines()

    figure(num=None, figsize=(30, 10), dpi=80, facecolor='w', edgecolor='k')

    i = 0
    x = list()
    y = list()
    for filetrans_time in filetrans_time_list:
        i = i + 1
        x.append(i)
        y.append(float(filetrans_time))

    plt.scatter(x, y)
    plt.plot(x, y)    
    plt.savefig(screenshot_file_full_path)
    # plt.show()

###### create post script
def create_post_script(channel_name, posting_user_name, target_text, emoji):
    return {"channel": channel_name, "username": posting_user_name, "text": target_text, "icon_emoji": emoji}

###### post a script
def post_to_a_channel(driver, requests_post_url, post_script):
    response = requests.post(requests_post_url, json=post_script)
    print "posting to slack response :",response.status_code

###### post a screenshot
def post_a_screenshot(screenshot_file_full_path, token, channels):
    files = {'file': open(screenshot_file_full_path, 'rb')}
    param = {'token':token, 'channels':channels}
    response = requests.post(url="https://slack.com/api/files.upload",params=param, files=files)
    print "response from post image to slack response :",response.status_code


### FUNC DEFINITION
#########################################################################################

create_filetrans_time_graph()
post_a_screenshot(screenshot_file_full_path, xxx_channel_info.get('token'), xxx_channel_info.get('channels'))
