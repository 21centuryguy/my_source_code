from urllib.request import urlopen

target_url = "https://www.yahoo.co.jp"
html = urlopen(target_url)
print(html.read())
