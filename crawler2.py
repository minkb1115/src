'''
Created on 2013. 10. 1.

@author: minkb
'''
import urllib
import urllib2
 
url = "http://www.soramoon.info/member/login.php"
login_form={"p_userid":"minkb","p_passwd":"3302"}
login_req=urllib.urlencode(login_form)
request=urllib2.Request(url,login_req)
print request
response = urllib2.urlopen(request)
cookie = response.headers.get('Set-Cookie')
 
data = response.read()
 
print cookie
 
 
url2 = "http://photo.soramoon.info/album/theme/pic_view.php?p_num=2063877&p_anum=999&p_option=&p_ix=1"
request2 = urllib2.Request(url2)
request2.add_header('cookie',cookie)
response2 = urllib2.urlopen(request2)
 
data2 = response2.read()
 
print data2
