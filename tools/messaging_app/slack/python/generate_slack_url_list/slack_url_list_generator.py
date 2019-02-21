import re
from slack_url_picker import main

def slack_url_list_generator():

	"""
	[1] This is main module. This module will call "slack_url_picker"
	[2] Before run this module, you have to prepare html data for worksapce url => "data/raw_data_01.txt", "data/raw_data_02.txt"
	[3] "data/raw_data_01.txt" -> html from "https://slack.com/signin/find"
	[4] "data/raw_data_02.txt" -> html from gmail mail -> html text should be line by line
	"""

	slack_worksapce_name_list = main()
	slack_worksapce_name_list = set(slack_worksapce_name_list)
	slack_worksapce_name_list = list(slack_worksapce_name_list)
	slack_worksapce_name_list.sort()

	f = open("result/my_slack_worksapce_url.html", mode="w+")
	for slack_worksapce_name in slack_worksapce_name_list:
		link = "<a href='https://" + slack_worksapce_name + ".slack.com'" + " target='_blank'>" + slack_worksapce_name + "</a>"
		f.write(link)
		f.write("\n<br>\n")
		print(link)

if __name__ == '__main__':
	slack_url_list_generator()
