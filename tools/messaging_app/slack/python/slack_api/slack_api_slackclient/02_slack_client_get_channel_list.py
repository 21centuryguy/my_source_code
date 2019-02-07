# CTEC 121 / Intro to Programming and Problem Solving
# Lab - Using the Slack API
# by Bruce Elgort, 2016
# https://github.com/belgort/python-slack-example/blob/master/slack_demo.py

# pip install slackclient to install SlackClient library
from slackclient import SlackClient
import json

#------------------------------------------------------------
# function definition

def get_list_of_channels(sc):
	channels = sc.api_call("channels.list")
	channels = json.dumps(channels)
	channels = json.loads(str(channels))
	print(121212121212)
	print(channels)
	print(121212121212)	
	return channels

def display_channels(channels):
	print("\n>>>>>>>   Channels List   <<<<<<<")
	print(40 * "=")
	for i in channels['channels']:
		print("Channel:",i['name'])
	print("\n\n\n")


def main(token, channel):
	# connect to Slack
	sc = SlackClient(token)

	# get list of channels
	channels = get_list_of_channels(sc)

	# display channels
	display_channels(channels)

#------------------------------------------------------------
# dic : slack hook url, token, channles
jack_api_test_channel_info = {
'slack_token':'xxx',
'channel_id':'xxx',
}

#------------------------------------------------------------
# variables setting
slack_token = jack_api_test_channel_info.get('slack_token')
channel = jack_api_test_channel_info.get('channel_id')

#------------------------------------------------------------
# function calling
main(slack_token, channel)
