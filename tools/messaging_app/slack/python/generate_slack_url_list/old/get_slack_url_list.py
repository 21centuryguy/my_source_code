import re

def get_workspace_name_from_mail():
	list_from_mail_raw =['dev4slack​​','teamlabatgachon​​','jacknrieko​​','bookingzhongxin​​','snszhongxin​​','aimldlmaster​​','mylifememories​​','manualzhongxin​​','linuxosmaster​​','dramazhongxin​​','myzasan​​','searchitnow​​','saramdeul​​','historyfact​​','currentprogress​​','androidmaster​​','hardwarezhongxin​​','organizethem​​','issuetrackingzhongxin​​','makethebetterworld​​','yibuyibuwangqianzou​​','animationzhongxin​​','geuridoeljieoda​​','iosmaster​​','goumaizhongxin​​','astronomyzhongxin​​','mypropertylist​​','dishuichuanshi​​','radiozhongxin​​','databasemaster​​','webdevmaster​​','yingyucigenmaster​​','mycloudkongjian​​','windowsmaster​​','sharezhongxin​​','apizhongxin​​','hamyeondoinda​​','pglang-python​​','mysnippets​​','projectzhongxin​​','searchzhongxin​​','schedulezhongxin​​','whereismysourcecode​​','understanditnow​​','myprocedure​​','manhwa​​','sourcecodesearch​​','mymisshistory​​','myroutinemyrule​​','norenore​​','isitok​​','mathzhongxin​​','encodingdecoding​​','cheatsheetszhongxin​​','postzhongxin​​','tvshowzhongxin​​','documentaryzhongxin​​','nationzhongxin​​','novelzhongxin​​','musiczhongxin​​','essenceofessence​​','appmakerzhongxin​​','datasciencezhongxin​​','cszhongxin​​','booksonweb​​','withfamily​​','yuyanzhongxin​​','crawlingzhongxin​​','jihuazhongxin​​','toolzhongxin​​','opensourcezhongxin​​']

	list_from_mail = []
	for xxx in list_from_mail_raw:
		xxx = xxx.replace(u'\u200b','')
		list_from_mail.append(xxx)

	# print("list_from_mail : \n", list_from_mail)
	# print("\n")
	list_from_mail.sort()
	# print(len(list_from_mail))
	# print("list_from_mail : \n", list_from_mail)
	# print("\n\n")

	return list_from_mail

def get_workspace_name_from_web():
	list_from_web_raw = ['dev4slack','miraitranslate','systraninternational','jacknrieko','pglang-python','toolzhongxin','opensourcezhongxin','youtubezhongxin','lecturezhongxin','booksonweb','apizhongxin','termiseverything','pglang','projectzhongxin','websitezhongxin','whathowwhy','mathzhongxin','understanditnow','tryitrightnow','todozhongxin','mysnippets','searchzhongxin','issuetrackingzhongxin','documentationzhongxin','saenggak','windowsmaster','macosmaster','androidmaster','tvzhongxin','suoyouwiki','softwarezhongxin','librarymaster','whatisdifference','tryitdirectly','comparethem','listofeverything','historyzhongxin','myxinxi','currentprogress','howtoinstall','tutorialzhongxin','guidezhongxin','historyfact','gamezhongxin','saramdeul','communityzhongxin','codeexamples','pathinfo','formatzhongxin','shortcutszhongxin','exerciseszhongxin','stackzhongxin','banbokpower','travelzhongxin','moviezhongxin','collectionzhongxin','dramazhongxin','essenceofessence','musiczhongxin','novelzhongxin','nationzhongxin','documentaryzhongxin','encodingdecoding','isitok','sourcecodesearch','manhwa','myprocedure','myzasan','appmakerzhongxin','linuxosmaster','cszhongxin','readitrightnow','datasciencezhongxin','learningmaster','aimldlmaster','snszhongxin','hardwarezhongxin','searchitnow','organizethem','yibuyibuwangqianzou','animationzhongxin','geuridoeljieoda','goumaizhongxin','astronomyzhongxin','mypropertylist','yingyucigenmaster','sharezhongxin']

	list_from_web = []
	for xxx in list_from_web_raw:
		xxx = xxx.strip(u'\u200b')
		list_from_web.append(xxx)

	# print("list_from_web : \n", list_from_web)
	# print("\n")
	list_from_web.sort()
	# print(len(list_from_web))
	# print("list_from_web : \n", list_from_web)
	# print("\n\n")

	return list_from_web

def get_workspace_name_from_web_n_email(list_from_mail, list_from_web):
	list_from_web_mail = []
	list_from_web_mail = list_from_web + list_from_mail

	list_from_web_mail_unique = set(list_from_web_mail)
	# print("list_from_web_mail_unique length : ", len(list_from_web_mail_unique))
	# print("list_from_web_mail_unique : \n", list_from_web_mail_unique)
	# print("\n\n")

	list_from_web_mail_unique_sorted = []
	for xxx in list_from_web_mail_unique:
		# print(xxx)
		list_from_web_mail_unique_sorted.append(xxx)
	
	# print("\n")
	# print("list_from_web_mail_unique_sorted : ", len(list_from_web_mail_unique_sorted))
	list_from_web_mail_unique_sorted.sort()
	# print("\n")
	# print("list_from_web_mail_unique_sorted : ", list_from_web_mail_un1ique_sorted)
	# print("\n")

	return list_from_web_mail_unique_sorted

def get_url_from_workspace_name(list_from_web_mail_unique_sorted):
	for xxx in list_from_web_mail_unique_sorted:
		url = xxx + ".slack.com"
		# print(url)

def get_link_from_workspace_url(list_from_web_mail_unique_sorted):
	f = open("./my_slack_worksapce_url.html", mode="w")
	for xxx in list_from_web_mail_unique_sorted:
		link = "<a href='https://" + xxx + ".slack.com'" + " target='_blank'>" + xxx + "</a>"
		f.write(link)
		f.write("<br>")
		print(link)

def main():
	list_from_mail = get_workspace_name_from_mail()
	list_from_web = get_workspace_name_from_web()
	list_from_web_mail_unique_sorted = get_workspace_name_from_web_n_email(list_from_mail, list_from_web)
	workspace_name_url = get_url_from_workspace_name(list_from_web_mail_unique_sorted)
	get_link_from_workspace_url(list_from_web_mail_unique_sorted)

if __name__ == '__main__':
	main()
