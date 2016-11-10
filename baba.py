import sys

html = sys.argv[1]
url = sys.argv[2]
title = sys.argv[3]
tuwel_url = sys.argv[4]

filename = title.replace(' ', '_')
try:
	with open(filename, 'r+') as f:
		content = f.read()
		if (content!=html):
			f.write(html)
			print tuwel_url
			exit(title)
except:
	with open(filename, 'wb') as f:
		f.write(html)
		#print tuwel_url
		exit(title)
