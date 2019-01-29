import httplib2, os
from apiclient import discovery
import gmail_auth # 先ほど作成したプログラム
import base64
import re

# Gmailのサービスを取得
def gmail_get_service():
    # ユーザー認証の取得
    credentials = gmail_auth.gmail_user_auth()
    http = credentials.authorize(httplib2.Http())
    # GmailのAPIを利用する
    service = discovery.build('gmail', 'v1', http=http)
    return service

def GetMimeMessage_1():
    service = gmail_get_service()
    messages = service.users().messages()
    msg_list = messages.list(userId='me', maxResults=10).execute()

    i = 1
    for msg in msg_list['messages']:
        topid = msg['id']
        try:
            print("="*100)
            print(">>> count : ", i)
            message = service.users().messages().get(userId='me', id=topid, format='raw').execute()
            print('Message snippet: %s' % message['snippet'])
            msg_str = base64.urlsafe_b64decode(message['raw'])
            msg_str = msg_str.decode('utf-8')
            msg_str2 = re.sub('<[^>]*>', '', msg_str) # 태그를 모두 삭제한다.
            # print(msg_str2)
            sep = 'Content-Type' # 타겟 스트링의 바로 아래의 첫 스트링을 삭제 기준으로 삼는다.
            msg_str3 = msg_str2.split(sep)[:-1][0] # 타겟스트링의 아래를 전부 잘라 버린다.
            print("-"*50)
            print(msg_str3[msg_str3.index('Subject:'):-1]) # 타겟 스트링의 첫글자위치부터 맨 끝까지 지정해서 가져온다 !!!
            print("\n\n")
        except Exception as error:
            print('An error occurred: %s' % error)
            print("\n\n")
        i = i + 1

def GetMimeMessage_2():
    service = gmail_get_service()
    messages = service.users().messages()
    msg_list = messages.list(userId='me', maxResults=10).execute()

    for msg in msg_list['messages']:
        topid = msg['id']
        try:
            print("="*100)
            message = service.users().messages().get(userId='me', id=topid, format='raw').execute()
            print('Message snippet: %s' % message['snippet'])
            msg_str = base64.urlsafe_b64decode(message['raw'])
            msg_str = msg_str.decode('utf-8')
            msg_str2 = re.sub('<[^>]*>', '', msg_str) # 태그를 모두 삭제한다.
            # print(msg_str2)
            print("\n\n")
            print("-"*50)
            
            date_start_position = msg_str2.index('Subject: ') # 프린트하고 싶은 부분의 스트링의 시작부분
            from_start_position = msg_str2.index('Message-ID:') # 프린트하고 싶은 부분이 끝나고 시작되는 부분 
            # print(date_start_position)
            # print(from_start_position)
            print(msg_str2[date_start_position:from_start_position])
            
        except Exception as error:
            print("="*100)            
            print('An error occurred: %s' % error)
            print("-"*50)

GetMimeMessage_1()
# GetMimeMessage_2()
