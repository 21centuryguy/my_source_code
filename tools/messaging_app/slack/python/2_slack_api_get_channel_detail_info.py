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

    print("\n\n" + 25 * "=" + "   Testing API ( response )  " + 25 * "=" + "\n")
    r = sc.api_call("api.test")
    r = json.dumps(dict(r), sort_keys=True, indent=3)
    print(r)
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
    print(channels)
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
    print(channel_name_list)
    print("\n\n\n")
    return channel_name_list






def get_channel_id(channels):
    """
    getting channel id
    [ for i in channels['channels']:
        channel_id = i['id']
        channel_id_list.append(channel_id) ]
    """

    channel_id_list = []
    print("\n\n" + 25 * "=" + "   Channels ID List ( handled )  " + 25 * "=" + "\n")
    for i in channels['channels']:
        channel_id = i['id']
        channel_id_list.append(channel_id)
    print(channel_id_list)
    print("\n\n\n")
    return channel_id_list






def get_channel_detail_info(sc, channel_id_list):
    """
    getting channel info
    [ sc.api_call("channels.info", channel=channel_id) ]
    """

    print("\n\n" + 25 * "=" + "   Every each Channel detail info ( raw )  " + 25 * "=" + "\n")
    for channel_id in channel_id_list:
        # print("="*10)
        # print(channel_id)
        # print("="*10)
        r = sc.api_call("channels.info", channel=channel_id)
        r = json.dumps(dict(r), sort_keys=True, indent=3)
        print(r)
        print("\n")
    print("\n\n\n")







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

    # --------- 2. get channel detail info
    get_channel_detail_info(sc, channel_id_list)

    # done
    print("-"*3 + " done " + "-"*3)

if __name__ == "__main__":

    #------------------------------------------------------------
    # dict : slack hook url, token, channles
    target_api_test_channel_info = {
    'channels_history_get_url':'https://slack.com/api/channels.history',
    'channels_file_list_url':'https://slack.com/api/files.list',
    'slack_token':{PUT YOUR SLACK TOKEN STRING HERE},
    }

    #------------------------------------------------------------
    # variables setting
    channels_history_get_url = target_api_test_channel_info.get('channels_history_get_url')
    channels_file_list_url = target_api_test_channel_info.get('channels_file_list_url')
    slack_token = target_api_test_channel_info.get('slack_token')

    #------------------------------------------------------------
    # function calling
    main(slack_token)
