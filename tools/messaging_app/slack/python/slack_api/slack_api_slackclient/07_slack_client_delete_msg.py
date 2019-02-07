from slackclient import SlackClient
import json

#------------------------------------------------------------
# dic : slack hook url, token, channles
jack_api_test_channel_info = {
'slack_token':'xxx',
'channel_id':'xxx',
'username':'jackmac',
'icon_url':'/Users/jack/Desktop/book.ico',
'text':'Hello from Python! :tada:'
}

#------------------------------------------------------------
# variables setting
slack_token = jack_api_test_channel_info.get('slack_token')
channel = jack_api_test_channel_info.get('channel_id')
username = jack_api_test_channel_info.get('username')
icon_url = jack_api_test_channel_info.get('icon_url')

# slack_token = os.environ["SLACK_API_TOKEN"]
sc = SlackClient(slack_token)

r = sc.api_call(
  "chat.delete",
  channel=channel,
  ts="1546760756.001100"
)

r = json.dumps(dict(r), sort_keys=True, indent=3)
print (r)
