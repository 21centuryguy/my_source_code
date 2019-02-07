import requests
import json


#------------------------------------------------------------
# function definition
def get_all_message(channels_history_get_url, slack_token, channels):
    url_options = "?token=" + slack_token + "&channel=" + channels + "&pretty=1"
    response = requests.get(channels_history_get_url + url_options)

    # response status code
    print("\n\n\n"+"1"*100)
    print("response status code : ",response.status_code)

    # response header
    response_headers = response.headers
    response_headers = json.dumps(dict(response_headers), sort_keys=True, indent=3)
    print("\n\n\n"+"2"*100)
    print(response_headers)

    # response content
    response_content = response.content
    response_content = response_content.decode('utf-8')
    response_content = json.dumps(response_content)
    response_content = json.loads(str(response_content))
    print("\n\n\n"+"3"*100)
    print(response_content)

def main():
    get_all_message(channels_history_get_url, slack_token, channels)


#------------------------------------------------------------
# dict : slack hook url, slack_token, channles
jack_api_test_channel_info = {
'channels_history_get_url':'https://slack.com/api/channels.history',
'slack_token':'xxx',
'channels':'xxx'
}

#------------------------------------------------------------
# variables
channels_history_get_url = jack_api_test_channel_info.get('channels_history_get_url')
slack_token = jack_api_test_channel_info.get('slack_token')
channels = jack_api_test_channel_info.get('channels')

#------------------------------------------------------------
# call function
main()


