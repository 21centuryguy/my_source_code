import re

def myfunction(file_path):
	f = open(file_path, mode="r")
	
	text_list = []
	a = 1; b = 1; c=1; d=1
	for text in f:
		if "http" in text:
			if "slack.com" in text:
				if "https://app.slack.com" not in text:
					# print("string with 'http', 'slack.com' and without 'https://app.slack.com' count : ", a)
					# print(text)
					start_point_keyword = '<a href="https://'; end_point_keyword = '.slack.com/'
					start_point = text.index(start_point_keyword); end_point = text.index(end_point_keyword)
					# print("start_point : ", start_point); print("end_point : ", end_point)
					text = text[start_point+len(start_point_keyword):end_point]
					print(text)
					text_list.append(text)
					a = a + 1
				else:
					# print("string without 'slack.com' count and with 'https://app.slack.com': ", b)
					b = b + 1
			else:
				# print("string without 'slack.com' count : ", c)
				c = c + 1
		else:
			# print("string without 'http' count : ", d)
			d = d + 1

	return text_list



def main():

	workspace_name_list_from_web = myfunction("data/raw_data_01.txt")
	workspace_name_list_from_mail = myfunction("data/raw_data_02.txt")
	total_workspace_name_list = workspace_name_list_from_web + workspace_name_list_from_mail

	print(len(workspace_name_list_from_web))
	print(len(workspace_name_list_from_mail))
	print(len(total_workspace_name_list))

	return total_workspace_name_list

if __name__ == '__main__':
	main()
