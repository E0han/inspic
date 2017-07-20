#Instagram Saver
#By 0han
#python 3.x
#coding=utf-8
import requests
from bs4 import BeautifulSoup

share_link=input("Share Link:\n")
def run(link):
	html_doc = requests.get(link)
	html_doc.encoding='utf-8'
	soup = BeautifulSoup(html_doc.text, 'html.parser')
	for meta in soup.select('meta'):
		if meta.get('property') == 'og:image':
			pic_link=meta.get('content')#picture's address
			pic_r=requests.get(pic_link)
			file=open("a.jpg","wb")
			file.write(pic_r.content)
			file.close()
		else:
			continue
run(share_link)