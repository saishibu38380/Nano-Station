
import urllib, urllib2, cookielib,time,json 
from dbwrite import todb
import time
user ='ubnt'
pswd='1234'
import ssl
pos=1
ssl._create_default_https_context = ssl._create_unverified_context
cj=cookielib.CookieJar()
opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
r=opener.open('https://192.168.179.107/login.cgi')
login_data=urllib.urlencode({'username':user, 'password':pswd,'action':'login'})
r=opener.open('https://192.168.179.107/login.cgi',login_data)
data=dict()
print "login success"
while(1):
	print "next set"
	status_page=opener.open('https://192.168.179.107/status.cgi')
	status=status_page.read()
#	print (status)
	json_status=json.loads(status)
	signal=json_status['wireless']['signal']
	noise=json_status['wireless']['noisef']
	ccq=json_status['wireless']['ccq']
	distance=json_status['wireless']['distance']
	print str(signal) + 'db'
	print str(noise) + 'db';
	print str(ccq) 
	print str(distance) + 'm'

	data={'signalstrength':signal,'noisefloor':noise,'pos':pos,'ccq':ccq,'distance':distance}
	todb(data)
	time.sleep(5)
	print "Data Stored"
	

