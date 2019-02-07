import re
from slack_url_picker import main

def slack_url_list_generator():
		slack_worksapce_name_list = main()
		f = open("result/my_slack_worksapce_url.html", mode="a+")
		for slack_worksapce_name in slack_worksapce_name_list:
			link = "<a href='https://" + slack_worksapce_name + ".slack.com'" + " target='_blank'>" + slack_worksapce_name + "</a>"
			f.write(link)
			f.write("\n<br>\n")
			print(link)

slack_url_list_generator()
