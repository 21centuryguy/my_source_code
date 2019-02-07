# CTEC 121 / Intro to Programming and Problem Solving
# Lab - Using the Slack API
# by Bruce Elgort, 2016
# https://github.com/belgort/python-slack-example/blob/master/slack_demo.py

# pip install slackclient to install SlackClient library
from slackclient import SlackClient
import json

#------------------------------------------------------------
# function definition

def get_channel_info(sc,channel):
	print(">>>>>>>   Channel Info   <<<<<<<")
	print(80 * "=")
	r = sc.api_call("channels.info", channel=channel)
	r = json.dumps(dict(r), sort_keys=True, indent=3)
	print(r)
	print("\n\n\n")

def main(token, channel):
	# connect to Slack
	sc = SlackClient(token)

	# get channel info
	get_channel_info(sc,channel)

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
