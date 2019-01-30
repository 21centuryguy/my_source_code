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

    # done
    print("-"*3 + " done " + "-"*3)






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

if __name__ == "__main__":

    #------------------------------------------------------------
    # variables setting
    channels_history_get_url = jack_api_test_channel_info.get('channels_history_get_url')
    channels_file_list_url = jack_api_test_channel_info.get('channels_file_list_url')
    slack_token = jack_api_test_channel_info.get('slack_token')

    #------------------------------------------------------------
    # function calling
    main(slack_token)
