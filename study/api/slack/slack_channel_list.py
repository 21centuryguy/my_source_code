channel_name_list = ["db-mariadb", "historyzhongxin", "tryitdirectly", "suoyouwiki", "isomaster", "timezhongxin", "youtubezhongxin", "opensourcezhongxin", "jihuazhongxin", "crawlingzhongxin", "yuyankongjian", "driverzhongxin", "apizhongxin", "dumpzhongxin", "pglang", "projectzhongxin", "websitezhongxin", "packagezhongxin", "networkzhongxin", "whathowwhy", "saenggak", "windowsmaster", "macosmaster", "Manhwazhongxin", "androidmaster", "whereismysourcecode", "whoarewewhoami", "tvzhongxin", "tryitrightnow", "todozhongxin", "comparethem", "mybooklist", "suoyoumeili", "automationzhongxin", "ivereadaboutitsir", "icontrolmylife", "currentprogress", "browserzhongxin", "searchzhongxin", "TeamLab At Gachon University", "family", "miraitranslate", "jack&rieko", "understanditnow", "natureorgod", "howtoinstall", "myxinxi", "imagezhongxin", "listofeverything", "whatisdifference", "librarymaster", "softwarezhongxin", "yeohaeng", "whowearewhoami", "masterlinux", "issuetrackingzhongxin", "documentationzhongxin", "myapplist", "mysnippets", "mathzhongxin", "xiazaizhongxin", "termiseverything", "booksonweb", "lecturezhongxin", "toolzhongxin", "pglang-python", "hamyeondoinda", "tutorialzhongxin"]
channel_name_list.sort()
channel_url_html_list = []

for channel_name in channel_name_list:
	channel_url_html = "<p><a href = 'https://" + channel_name + ".slack.com'>" + channel_name + "</a></p>"
	# channel_url_html_list.append(channel_url_html)
	print(channel_url_html)
