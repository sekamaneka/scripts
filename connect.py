def save_cookies(requests_cookiejar, filename):
    with open(filename, 'wb') as f:
        pickle.dump(requests_cookiejar, f)
def load_cookies(filename):
    with open(filename, 'rb') as f:
        return pickle.load(f)
import requests
import pickle
import sys
s = requests.Session()
try:
	tuwel_url = sys.argv[1]
	url = sys.argv[2]
	title = sys.argv[3]
except:
	print('NOTWORKING')
try:
	s.cookies = load_cookies('tuwel_cookies')
except:
	print('ITSNOTWORKING')
	app_number = 36
	#36 for tuwel, 76 for tiss
	data = {"pw":"", "name":"", "totp":"", "app":app_number}
	url = 'https://iu.zid.tuwien.ac.at/AuthServ.portal'
	r = s.post(url, data=data)
r = s.get(tuwel_url)
#s holds the session
#r holds the relevant website data
print(r.text.encode('utf8', 'replace'))
#can e nter another data object in the text

print('<bookstore ' + 'url=https://tiss.tuwien.ac.at' +url+ ' tuwel_url='+tuwel_url+" title='"+title+"'></bookstore>")

#the cookies are saved in a file called tuwel_cookies
save_cookies(s.cookies, 'tuwel_cookies')





#div id="contentForm:groupPanel"
