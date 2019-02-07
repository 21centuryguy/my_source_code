"https://slack.com/signin/find" # url
"//*[@id="form_body"]/div" # xpath 워크스페이스 리스트 >> 가공이 필요 >> <a href="https부터 .slack.com까지 긁오온다 ( 반복해서 다 )

"//*[@class="signed_in_team_name"]" # 다른 워크스페이스를 찾기 위한 링크 >> 클릭

"//*[@id="email_input"]" # 위의 링크 클릭한 후에 >> 여기 이메일 텍스트 박스에 이메일을 입력한다 >> "uvmaker@gmail.com"

"//*[@id="submit_btn_label_single"]" >> 위의 이메일 입력 후 >> send 이메일 버튼을 클릭한다

"https://gmail.com/" # 으로 액세스한다


//*[@id=":2i"] # 지메일 첫번째 메시지를 연다
>> 쉽지 않을 거 같은데...
첫번째 //*[@id=":2b"]/tbody
//*[@id=":2d"]
#\:2d
//*[@id=":2c"]/td[5]
#\:2c > td.yX.xY
>> 정 안되면, 지메일 내용 복사헤서 파일에서 저장하는 거까지는 수동으로 하자.
이렇게만 하면, 읽어들여서 필요한 부분만 뽑아서 리스트로 저정해서 ~~~


"/html/body" # 그냥 바디 전체의 텍스트를 가져오다 >> <a href="https부터 .slack.com까지 긁오온다 ( 반복해서 다 )









