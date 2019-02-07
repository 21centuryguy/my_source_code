# CTEC 121 / Intro to Programming and Problem Solving
# Lab - Using the Slack API
# by Bruce Elgort, 2016
# https://github.com/belgort/python-slack-example/blob/master/slack_demo.py

# pip install slackclient to install SlackClient library
from slackclient import SlackClient
import json

#------------------------------------------------------------
# function definition
def post_message(sc, text, channel, icon_url, username):
	print("Posting Message to Slack")
	print(80 * "=")
	# post a message into the #general channel
	r = sc.api_call(
		"chat.postMessage",
		channel=channel,
		text=text,
		username=username,
		icon_url=icon_url,
		unfurl_links="true")
	r = json.dumps(dict(r), sort_keys=True, indent=3)
	print (r)
	print("\n\n\n")

def main(slack_token, channel, username, icon_url):
	# connect to Slack
	sc = SlackClient(slack_token)

	# post message
	post_message(sc,"Visit http://slack.com", channel, username, icon_url)

#------------------------------------------------------------
# dic : slack hook url, token, channles
jack_api_test_channel_info = {
'slack_token':'xxx',
'channel_id':'xxx',
'username':'jackmac_python',
'icon_url':'/Users/jack/Desktop/book.ico',
'text':'Hello from Python! :tada:'
}

#------------------------------------------------------------
# variables setting
slack_token = jack_api_test_channel_info.get('slack_token')
channel = jack_api_test_channel_info.get('channel_id')
username = jack_api_test_channel_info.get('username')
icon_url = jack_api_test_channel_info.get('icon_url')


#------------------------------------------------------------
# function calling
main(slack_token, channel, username, icon_url)
