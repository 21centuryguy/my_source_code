"""
todo : gui
"""

from slackclient import SlackClient
import requests
import json
import time

#------------------------------------------------------------
# function definition

def test_slack(sc):
    """
    debugging
    [ sc.api_call("api.test") ]
    """

    print("\n\n" + 25 * "=" + "   Testing API   " + 25 * "=" + "\n")
    r = sc.api_call("api.test")
    r = json.dumps(dict(r), sort_keys=True, indent=3)
    print(r)
    print("\n\n\n")

def get_list_of_channels(sc):
    """
    getting channel list
    [ sc.api_call("channels.list" ]
    """

    channels = sc.api_call("channels.list")
    channels_json = json.dumps(channels, sort_keys=True, indent=3)
    # print("\n\n" + 25 * "=" + "   Channels List ( raw )  " + 25 * "=" + "\n")
    # print(channels_json)

    channels = json.dumps(channels)
    channels = json.loads(str(channels))
    # print("\n\n\n")
    return channels

def get_channels_name(channels):
    """
    getting channel list
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
    # print("\n\n\n")
    return channel_id_list

def get_channel_id(channels):
    """
    getting channel id
    [ for i in channels['channels']:
        channel_id = i['id']
        channel_id_list.append(channel_id) ]
    """

    channel_id_list = []
    print("\n\n" + 25 * "=" + "   Channels ID ( handled )  " + 25 * "=" + "\n")
    for i in channels['channels']:
        channel_id = i['id']
        channel_id_list.append(channel_id)
    # print(channel_id_list)
    # print("\n\n\n")
    return channel_id_list

def get_channel_info(sc, channel_id_list):
    """
    getting channel info
    [ sc.api_call("channels.info", channel=channel_id) ]
    """

    # print("\n\n" + 25 * "=" + "   Channel Info ( raw )  " + 25 * "=" + "\n")
    for channel_id in channel_id_list:
        # print("="*10)
        # print(channel_id)
        # print("="*10)
        r = sc.api_call("channels.info", channel=channel_id)
        r = json.dumps(dict(r), sort_keys=True, indent=3)
        # print(r)
        # print("\n")
    print("\n\n\n")

def get_all_message(channels_history_get_url, slack_token, channel_id_list):
    """
    get_all_message
    [ response = requests.get(channels_history_get_url + url_options) ]
    """

    text_list = []
    ts_list = []
    # print("\n\n" + 25 * "=" + "   get_all_message ( raw )  " + 25 * "=" + "\n")
    print("\n" + 25 * "=" + "   get_all_message ( handled )  " + 25 * "=" + "\n")
    for channel_id in channel_id_list:
        time.sleep(0.7)
        url_options = "?token=" + slack_token + "&channel=" + channel_id + "&pretty=1"
        response = requests.get(channels_history_get_url + url_options)

        #-- response status code
        print("\n\n\n\n\n\n\n\n\n"+"#"*30)
        print("response status code : ", response.status_code)
        print("#"*30 + "\n")

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
                # print(i)
                text = i['text']
                ts = i['ts']

                text = text.encode('utf-8')
                text = text.decode('utf-8')
                f = open("msg_ts_dict2.py", mode="a+")
                channel_id_mark = "\n\n" + "="*50 + "\n" + "="*7 + " [     " + channel_id + "     ] ( " + str(x) + " ) " + "="*7 + "\n" + "="*50 + "\n\n"
                text_ts = text + "\n" + ts + "\n\n"
                print(channel_id_mark)
                print(text_ts)
                f.write(channel_id_mark)
                f.write(text_ts)
                f.close()
                text_list.append(text)
                ts_list.append(ts)

                x = x + 1
        except Exception:
            print("\n\n\n" + "-_- "*25)
            print("\n" + channel_id + "is skipped" + "\n")
            print("-_- "*25 + "\n\n\n")

def main(slack_token):
    """
    main
    """

    # connect to Slack
    sc = SlackClient(slack_token)

    # test slack
    test_slack(sc)

    # get list of channels
    channels = get_list_of_channels(sc)

    # get channels id
    channel_id_list = get_channel_id(channels)

    # get channels name
    channel_name_list = get_channels_name(channels)

    # get channel info
    get_channel_info(sc, channel_id_list)

    # get all message
    get_all_message(channels_history_get_url, slack_token, channel_id_list)

    # done
    print("-"*3 + " done " + "-"*3)

if __name__ == "__main__":

    #------------------------------------------------------------
    # dict : slack hook url, token, channles
    target_channel_info = {
    'channels_history_get_url':'https://slack.com/api/channels.history',
    'slack_token':'YOUR SLACK TOKEN'
    }

    #------------------------------------------------------------
    # variables setting
    channels_history_get_url = target_channel_info.get('channels_history_get_url')
    slack_token = target_channel_info.get('slack_token')

    #------------------------------------------------------------
    # function calling
    main(slack_token)
