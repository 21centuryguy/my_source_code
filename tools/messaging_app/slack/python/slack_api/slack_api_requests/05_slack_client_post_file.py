import requests
import json

#------------------------------------------------------------
# path
screenshot_folder_path = "./"
screenshot_file_name = "image.png"
screenshot_file_full_path = screenshot_folder_path + screenshot_file_name

#------------------------------------------------------------
# function definition
def post_a_screenshot(screenshot_save_fullpath, slack_token, channels):
    files = {'file': open(screenshot_save_fullpath, 'rb')}
    param = {'token':slack_token, 'channels':channels}
    response = requests.post(url="https://slack.com/api/files.upload",params=param, files=files)

    # response status code
    print("\n\n\n"+"1"*100)
    print("file posting response :",response.status_code)

    # response headers
    response_headers = response.headers
    response_headers = json.dumps(dict(response_headers), sort_keys=True, indent=3)
    print("\n\n\n"+"2"*100)
    print(response_headers)

    # response contents
    response_content = response.content
    response_content = response_content.decode('utf-8')
    response_content = json.loads(response_content)
    response_content = json.dumps(dict(response_content), sort_keys=True, indent=3)
    print("\n\n\n"+"3"*100)
    print("response_content : ",response_content)

#------------------------------------------------------------
# dic about slack hook url, slack_token, channles
jack_api_test_channel_info = {
'slack_token':'xoxp-472537903685-472337934962-518875974054-d98e72006ceb97137eb8eb7d02d08987',
'channels':'CF424G7RB'}

#------------------------------------------------------------
# variables
channels = jack_api_test_channel_info.get('channels')
slack_token = jack_api_test_channel_info.get('slack_token')
files = screenshot_file_full_path

#------------------------------------------------------------
# call function
post_a_screenshot(screenshot_file_full_path, slack_token, channels)
