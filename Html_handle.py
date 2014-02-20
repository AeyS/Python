#coding: utf-8
'''======import_list========
    
    <none>'''

def dowpic():
	import urllib
	while True:
		pic_link = raw_input('pic_link:')
		if pic_link is '': break
		pic_link = __pic_link_big(pic_link)
		pic = urllib.urlopen(pic_link).read()
		f = open('C:/Users/TOM/Desktop/ps/%s' % pic_link.split('/')[-1],'wb')
		f.write(pic)
		f.close()

def __pic_link_big(pic_link):
	if len(pic_link.split('.')[-2])<=7:
		return pic_link.replace(pic_link.split('.')[-2]+'.','')
	else: return pic_link
