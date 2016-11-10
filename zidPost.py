def save_cookies(requests_cookiejar, filename):
	with open(filename, 'wb') as f:
		pickle.dump(requests_cookiejar, f)
def load_cookies(requests_cookiejar, filename):
	with open(filename, 'rb') as f:
		return pickle.load(f)
import requests
import sys
import pickle
s = requests.Session()
app_number = 76
#36 for tuwel
try:
	s.cookies = load_cookies('tiss_cookies')
except:
	data = {"pw":"", "name":"", "totp":"", "app":app_number}
	url = 'https://iu.zid.tuwien.ac.at/AuthServ.portal'
	r = s.post(url, data=data)

r = s.get('https://tiss.tuwien.ac.at/education/favorites.xhtml')
#print s.cookies
print(r.text.encode('utf8', 'replace'))
save_cookies(s.cookies, 'tiss_cookies')






#div id="contentForm:groupPanel"
