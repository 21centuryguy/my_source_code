# CTEC 121 / Intro to Programming and Problem Solving
# Lab - Using the Slack API
# by Bruce Elgort, 2016
# https://github.com/belgort/python-slack-example/blob/master/slack_demo.py

# pip install slackclient to install SlackClient library
from slackclient import SlackClient
import json

#------------------------------------------------------------
# function definition
def test_slack(sc):
	# use for debugging
	print("\nTesting API")
	print(80 * "=")
	r = sc.api_call("api.test")
	r = json.dumps(dict(r), sort_keys=True, indent=3)
	print(r)
	print("\n\n\n")

def main(slack_token):
	# connect to Slack
	sc = SlackClient(slack_token)

	# test slack
	test_slack(sc)

#------------------------------------------------------------
# dic : slack hook url, token, channles
jack_api_test_channel_info = {
'slack_token':'xxx'
}

#------------------------------------------------------------
# variables setting
slack_token = jack_api_test_channel_info.get('slack_token')

#------------------------------------------------------------
# function calling
main(slack_token)
