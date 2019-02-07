# CTEC 121 / Intro to Programming and Problem Solving
# Lab - Using the Slack API
# by Bruce Elgort, 2016
# https://github.com/belgort/python-slack-example/blob/master/slack_demo.py

# pip install slackclient to install SlackClient library
from slackclient import SlackClient
import json

#------------------------------------------------------------
# function definition
def get_users(sc):
	print("Get Users")
	print(80 * "1")
	#call the users.list api call and get list of users
	users = (sc.api_call("users.list"))
	users = json.dumps(dict(users), sort_keys=True, indent=3)
	print("users : ", users)
	print("\n\n\n")
	users = json.loads(str(users))
	return users

def display_users(sc,users):
	print("User List")
	print(80 * "3")
	# display active users
	for i in users['members']:
		# don't display slackbot
		if i['profile']['real_name'] != "slackbot":
			# don't display deleted users
			if not i['deleted']:
				# display real name
				print (i['profile']['real_name'])
	print("\n\n\n")

def main(slack_token):
	# connect to Slack
	sc = SlackClient(slack_token)

	# get users
	users = get_users(sc)

	# display users
	display_users(sc,users)

#------------------------------------------------------------
# dic : slack_token
jack_api_test_channel_info = {
'slack_token':'xxx'
}

#------------------------------------------------------------
# variables setting
slack_token = jack_api_test_channel_info.get('slack_token')

#------------------------------------------------------------
# function calling
main(slack_token)
