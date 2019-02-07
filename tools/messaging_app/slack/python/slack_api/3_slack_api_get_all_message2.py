"""
todo : gui
"""

from slackclient import SlackClient
import requests
import json
import time
from slack_info import *

#------------------------------------------------------------
# function definition

def test_slack(sc):
    """
    debugging
    [ sc.api_call("api.test") ]
    """

    print("\n\n" + 25 * "=" + "   Testing API ( response )  " + 25 * "=" + "\n")
    r = sc.api_call("api.test")
    r = json.dumps(dict(r), sort_keys=True, indent=3)
    # print(r)
    print("\n\n\n")







def get_all_channels_list_n_info(sc):
    """
    get_all_channels_list_n_info
    [ sc.api_call("channels.list" ]
    """

    print("\n\n" + 25 * "=" + "   All_channels_list_n_info ( raw )  " + 25 * "=" + "\n")
    channels = sc.api_call("channels.list")
    channels_json = json.dumps(channels, sort_keys=True, indent=3)
    # print("\n\n" + 25 * "=" + "   Channels List ( raw )  " + 25 * "=" + "\n")
    # print(channels_json)

    channels = json.dumps(channels)
    channels = json.loads(str(channels))
    # print(channels)
    print("\n\n\n")
    return channels






def get_channels_name(channels):
    """
    getting channel name
    [ for i in channels['channels']:
        channel_name = i['name']
        channel_name_list.append(channel_name) ]
    """

    channel_name_list = []
    print("\n\n" + 25 * "=" + "   Channels Name List ( handled )  " + 25 * "=" + "\n")
    for i in channels['channels']:
        channel_name = i['name']
        channel_name_list.append(channel_name)
    # print(channel_name_list)
    print("\n\n\n")
    return channel_name_list






def get_channel_id(channels):
    """
    getting channel id
    [ for i in channels['channels']:
        channel_id = i['id']
        channel_id_list.append(channel_id) ]
    """

    myoption = 1

    channel_id_list = []
    print("\n\n" + 25 * "=" + "   Channels ID List ( handled )  " + 25 * "=" + "\n")
    for i in channels['channels']:
        channel_id = i['id']

        if myoption == 1:
            if channel_id== 'CEJUP04C8':
                channel_id_list.append(channel_id)
        if myoption == 2:
            channel_id_list.append(channel_id)

    print(channel_id_list)
    print("\n\n\n")
    return channel_id_list







def get_all_message(channels_history_get_url, slack_token, channel_id_list):
    """
    get_all_message
    [ response = requests.get(channels_history_get_url + url_options) ]
    """

    text_list = []
    ts_list = []
    print("\n" + 25 * "=" + "   get_all_message ( handled )  " + 25 * "=" + "\n")
    for channel_id in channel_id_list:
        time.sleep(0.7)

        while_loop_count = 1
        request_response = True
        url_options = "?token=" + slack_token + "&channel=" + channel_id + "&count=10" + "&inclusive=1" + "&pretty=1"
        while request_response == True:
            print("while_loop_count : ", while_loop_count)
            response = requests.get(channels_history_get_url + url_options)

            #-- response status code
            print("\n"+"#"*30)
            print("response status code : ", response.status_code)
            print("#"*30 + "\n")

            if response.status_code == 200:
                request_response = True
                print(" current_request_response : ", request_response)

                #-- response header
                response_headers = response.headers
                response_headers = json.dumps(dict(response_headers), sort_keys=True, indent=3)
                # print("\n\n"+"="*100)
                # print(response_headers)

                #-- response content
                response_content = response.content
                response_content = response_content.decode('utf-8')    
                response_content = json.loads(response_content)
                # print("\n\n"+"="*100)
                # print(response_content)

                try:
                    x = 1
                    for i in response_content['messages']:
                    # for i in reversed(response_content['messages']):
                        # print(i)
                        text = i['text']
                        ts = i['ts']
        
                        text = text.encode('utf-8')
                        text = text.decode('utf-8')
                        f = open("msg_ts_dict.py", mode="w+")
                        channel_id_mark = "\n\n" + "="*50 + "\n" + "="*7 + " [     " + channel_id + "     ] ( " + str(x) + " ) " + "="*7 + "\n" + "="*50
                        text_ts = text + "\n" + ts + "\n\n"
                        print(channel_id_mark)
                        print("while_loop_count : ", while_loop_count)
                        print("\n\n" + text_ts)
                        f.write(channel_id_mark)
                        f.write(text_ts)
                        f.close()
                        text_list.append(text)
                        ts_list.append(ts)
                        x = x + 1 
                        
                except Exception as e:
                    print("\n\n\n" + "-_- "*25)
                    print("\n" + channel_id + "is skipped" + "\n")
                    print("error :", e)
                    print("-_- "*25 + "\n\n\n")

                while_loop_count = while_loop_count + 1
                url_options = "?token=" + slack_token + "&channel=" + channel_id + "&count=10" + "&latest=" + str(ts)  + "&inclusive=1" + "&pretty=1"

                assert len(response_content['messages']) == 10, "done !"

            else:
                request_response = False
                print("request_response = False. while loop has borken.")



def main(slack_token):
    """
    main
    """

    # --------- connect to Slack
    sc = SlackClient(slack_token)

    # --------- test slack
    test_slack(sc)

    # --------- 0. get_all_channels_list_n_info
    channels = get_all_channels_list_n_info(sc)

    # --------- 1. get channels id and name
    channel_id_list = get_channel_id(channels)
    channel_name_list = get_channels_name(channels)

    # --------- 3. get all message
    get_all_message(channels_history_get_url, slack_token, channel_id_list)

    # done
    print("-"*3 + " done " + "-"*3)

if __name__ == "__main__":

    #------------------------------------------------------------
    # variables setting
    channels_history_get_url = jack_api_test_channel_info.get('channels_history_get_url')
    channels_file_list_url = jack_api_test_channel_info.get('channels_file_list_url')
    slack_token = jack_api_test_channel_info.get('slack_token')

    #------------------------------------------------------------
    # function calling
    main(slack_token)
