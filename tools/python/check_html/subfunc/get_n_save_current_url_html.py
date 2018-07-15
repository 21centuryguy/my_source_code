def get_current_url_html(current_url):
	html = urlopen(current_url)
	bsObj = BeautifulSoup(html.read(), "html.parser")
	# print(bsObj)

	crawled_html_file_full_path = "/Users/jack/Desktop/" + current_url.replace(':','').replace('//','/').replace('/','_') + strftime("%Y%m%d_%H%M%S", localtime()) + ".txt"
			with open(crawled_html_file_full_path, 'w') as f:
		f.write(str(bsObj))
		f.close()