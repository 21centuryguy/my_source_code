import codecs
import re

outputf = open("./ip_list.txt", mode="w+")
inputf = open("./btmp", mode="rb")
lines = inputf.readlines()
for line in lines:
	line = line.decode('ascii', "ignore")
	line = line.replace('\0', '')
	ipPattern = re.compile('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	ip_list = re.findall(ipPattern,line)
	# print(ip_list)
	for ip in ip_list:
		outputf.write(ip)
		outputf.write('\n')
inputf.close()
outputf.close()
