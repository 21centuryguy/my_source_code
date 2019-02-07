import codecs
import re

outputf = open("./output/btmp_output.txt", mode="w+")
inputf = open("./input/btmp", mode="rb")
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

ip_list = []
outputf = open("./output/uniq_ip_list.txt", mode="w+")
inputf = open("./output/btmp_output.txt", mode="r")
lines = inputf.readlines()
for line in lines:
	# print(line)
	line = line.strip('\n')
	ip_list.append(line)
uniq_ip_list = list(set(ip_list))
uniq_ip_list.sort()
print(uniq_ip_list)

for ip in uniq_ip_list:
	outputf.write(ip)
	outputf.write('\n')
inputf.close()
outputf.close()