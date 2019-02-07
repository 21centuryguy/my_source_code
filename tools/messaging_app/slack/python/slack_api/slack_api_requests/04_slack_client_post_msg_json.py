import requests
import json

#------------------------------------------------------------
# dic about slack hook url, token, channles

jack_api_test_channel_info = {
'requests_post_url':'xxx',
'channels':'xxx',
'text':'<!channel> ```slack_api.py``` \nThis is a `test` messgae. :smile:'}

#------------------------------------------------------------
# function definition
def create_post_script(channels, target_text):
    return {"channel": channels, "text": target_text}

def post_a_message(requests_post_url, post_script):
    response = requests.post(requests_post_url, json=post_script)

    # print response status code
    print("\n"+"1"*30)
    print("response status code : ",response.status_code)

    # print response header
    print("\n\n\n"+"2"*30)
    header = response.headers
    header = json.dumps(dict(header), sort_keys=True, indent=3)
    # header = json.loads(str(header))
    print("response headers : ",header)

    # print response content
    print("\n\n\n"+"3"*30)
    content = response.content
    content = content.decode('utf-8')
    print("response contents : ",content)

#------------------------------------------------------------
# variables
requests_post_url = jack_api_test_channel_info.get('requests_post_url')
target_text = jack_api_test_channel_info.get('text')
channels = jack_api_test_channel_info.get('channels')

#------------------------------------------------------------
# call function
post_script = create_post_script(channels, target_text)
post_a_message(requests_post_url, post_script)
