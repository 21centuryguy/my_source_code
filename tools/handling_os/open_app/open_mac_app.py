import subprocess

def open_apps_sub_popen():
	"""
	[ subprocess.call ] 동시에 2개 이상 열 수 있어
	"""

	p1 = file_path = "/Users/jack/Desktop/"
	subprocess.Popen(["/usr/bin/open", "-W", "-n", "-a", "/Applications/PyCharm CE.app",file_path])

	p2 = file_path = "/Users/jack/Desktop/test.html"
	subprocess.Popen(["/usr/bin/open", "-W", "-n", "-a", "/Applications/TextEdit.app",file_path])

	p1.terminate()
	p2.terminate()


def open_apps_sub_call():
	"""
	[ subprocess.call ] 동시에 2개 이상 못 열어
	"""
	p1 = file_path = "/Users/jack/Desktop/test.html"
	subprocess.call(["/usr/bin/open", "-W", "-n", "-a", "/Applications/PyCharm CE.app",file_path])

	p2 = file_path = "/Users/jack/Desktop/test.html"
	subprocess.call(["/usr/bin/open", "-W", "-n", "-a", "/Applications/TextEdit.app",file_path])


open_apps_sub_popen()
# open_apps_sub_call()
